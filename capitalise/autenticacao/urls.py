from django.urls import path

from autenticacao.views import login, logout

urlpatterns = [
    path('abacate', login, name='login'),
    path('logout', logout, name='logout')
]