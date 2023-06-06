from django import forms
from .models import Carteira, Acao

class CriarCarteiraForm(forms.ModelForm):
    class Meta:
        model = Carteira
        fields = '__all__'

class AdicionarAtivoForm(forms.ModelForm):
    class Meta:
        model = Acao
        fields = '__all__'
