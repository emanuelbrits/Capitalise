from django.contrib import admin
from .models import Usuario, Carteira, Acao, Cotacao, Dividendo, Compra, Venda
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Carteira)
admin.site.register(Acao)
admin.site.register(Cotacao)
admin.site.register(Dividendo)
admin.site.register(Compra)
admin.site.register(Venda)