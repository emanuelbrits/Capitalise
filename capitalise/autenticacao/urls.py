from django.urls import path

from autenticacao.views import login, logout, cadastro

urlpatterns = [
    path('', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout')
]