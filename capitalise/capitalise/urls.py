from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('autenticacao.urls')),
    path('', include('cadastro.urls')),
    path('', include('app.urls')),
    path('admin/', admin.site.urls),
]
