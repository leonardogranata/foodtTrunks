from django.contrib import admin
from .models import Cliente, Produto, ItemVenda, Venda, LocalAtendimento

admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(LocalAtendimento)
admin.site.register(Venda)
admin.site.register(ItemVenda)
