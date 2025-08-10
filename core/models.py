from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=75)
    telefone = models.CharField(max_length=18)
    email = models.EmailField(unique=True)
    data_cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=40)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=4, decimal_places=2)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class LocalAtendimento(models.Model):
    nome = models.CharField(max_length=40)
    endereco = models.CharField(max_length=80)
    data_evento = models.DateField(blank=True, null=True)
    horario_inicio = models.TimeField(blank=True)
    horario_fim = models.TimeField(blank=True)

    def __str__(self):
        return f"{self.nome} - {self.data_evento}"
    
class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete= models.SET_NULL, null=True)
    local = models.ForeignKey(LocalAtendimento, on_delete=models.SET_NULL, null=True)
    data_venda = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente.nome} - {self.data_venda}"

    @property
    def total_vendas(self):
        return sum(item.total_vendas for item in self.itens.all())

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.SET_NULL, related_name='itens', null=True)
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.produto.nome} x {self.quantidade}"
    
    @property
    def subtotal(self):
        return self.quantidade * self.preco_unitario

