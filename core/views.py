from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Cliente, Produto, ItemVenda, Venda, LocalAtendimento
from django.db.models import Sum
from datetime import date

@login_required
def home(request):
    return render(request, 'core/home.html')

@login_required
def lista_produtos(request):
    produtos = Produto.objects.filter(ativo=True)
    return render(request, 'core/lista_produtos.html', {'produtos': produtos})

@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all().order_by('-data_cadastro')
    return render(request, 'core/lista_clientes.html', {'clientes': clientes})

@login_required
def lista_agenda(request):
    agenda = LocalAtendimento.objects.all().order_by('data_evento')
    return render(request, 'core/lista_agenda.html', {'agenda': agenda})

@login_required
def faturamento_mensal(request):
    ano = int(request.GET.get('ano', date.today().year))
    mes = int(request.GET.get('mes', date.today().month))

    vendas = Venda.objects.filter(data_venda__year=ano, data_venda__month=mes)
    total = Sum(venda.total_venda for venda in vendas)

    return render(request, 'core/faturamento_mensal.html', {
        'vendas': vendas,
        'total': total,
        'ano': ano,
        'mes': mes,
    })

@login_required
def produtos_mais_vendidos(request):
    produtos = (
        Produto.objects.annotate(
            quantidade_vendida = Sum('itemvenda__quantidade')
        )
        .order_by('-quantidade_vendida')[:10]
    )
    return render(request, 'core/produtos_mais_vendidos.html', {'produtos': produtos})

@login_required
def grafico_produtos_mais_vendidos(request):
    produtos = (
        Produto.objects.annotate(
            quantidade_vendida = Sum('itemvenda__quantidade')
        )
        .order_by('-quantidade_vendida')[:5]
    )
    labels = [prod.nome for prod in produtos]
    data = [int(prod.quantidade_vendida or 0) for prod in produtos]

    return render(request, 'core/grafico_produtos_mais_vendidos.html', {'labels': labels, 'data': data})


@login_required
def portifolio_produtos(request):
    produtos = Produto.objects.filter(ativo=True)
    return render(request, 'core/portifolio_produtos.html', {'produtos': produtos})
