from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produtos/', views.lista_produtos, name='produtos'),
    path('clientes/', views.lista_clientes, name='cliente'),
    path('agenda/', views.lista_agenda, name='agenda'),
    path('faturamento/', views.faturamento_mensal, name='faturamento'),
    path('mais_vendidos/', views.produtos_mais_vendidos, name='maisVendidos'),
    path('grafico_produtos/', views.grafico_produtos_mais_vendidos, name='graficoProdutos'),
    path('portifolio-produtos/', views.portifolio_produtos, name='portifolioProdutos'),
]
