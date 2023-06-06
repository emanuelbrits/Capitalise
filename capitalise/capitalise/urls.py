from django.contrib import admin
from django.urls import path
from app.views import criar_carteira, adicionar_ativo, visualizar_carteira

urlpatterns = [
    path('admin/', admin.site.urls),
    path('criar_carteira/', criar_carteira, name='criar_carteira'),
    path('adicionar_ativo/', adicionar_ativo, name='adicionar_ativo'),
    path('visualizar_carteira/', visualizar_carteira, name='visualizar_carteira'),
]
