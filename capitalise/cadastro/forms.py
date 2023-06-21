from django import forms

class CadastroForms(forms.Form):
    nome=forms.CharField(
        label='Usuário',        
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nome'
            }
        )
    )
    cpf=forms.CharField(
        label='CPF',        
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'CPF',
                'icon': 'ph-lock'
            }
        )
    )
    telefone=forms.CharField(
        label='Telefone',        
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Telefone',
                'icon': 'ph-lock'
            }
        )
    )
    email=forms.CharField(
        label='Email',        
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email'            
            }
        )
    )
    senha=forms.CharField(
        label='Senha',        
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '•••••••••••'
            }
        )
    )


