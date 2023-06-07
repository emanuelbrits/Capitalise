from django import forms
from .models import Carteira, Acao, Usuario

class CriarCarteiraForm(forms.ModelForm):
    class Meta:
        model = Carteira
        fields = '__all__'

class AdicionarAtivoForm(forms.ModelForm):
    class Meta:
        model = Acao
        fields = '__all__'

class UsuarioForm(forms.Form):
    id_usuario = forms.IntegerField(
        required=True,
        widget=forms.HiddenInput()
    )     
    nome=forms.CharField(
        label="Nome:",
        required=True,
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'            
            }
        )
    )  
    cpf=forms.CharField(
        label="CPF:",
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'            
            }
        )
    )      
    telefone=forms.CharField(
        label="Telefone:",
        required=True,
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'            
            }
        )
    ) 
    email=forms.CharField(
        label="Telefone:",
        required=True,
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'            
            }
        )
    ) 
    senha=forms.CharField(
        label="Telefone:",
        required=True,
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'            
            }
        )
    ) 