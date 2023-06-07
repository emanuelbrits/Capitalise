from django.urls import path
from app.views import *

urlpatterns = [
    path('usuario', usuario, name='usuario'),
]