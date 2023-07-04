from django import forms

class LoginForms(forms.Form):
    usuario=forms.CharField(
        label='Usuário',        
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'icon': 'ph-user-circle'
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
                'placeholder': '•••••••••••',
                'icon': 'ph-lock'
            }
        )
    )

class CadastroForms(forms.Form):
    email=forms.CharField(
        label='Email',        
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'icon': 'ph-user-circle'
            }
        )
    )
    nome=forms.CharField(
        label='Nome',        
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nome',
                'icon': 'ph-user-circle'
            }
        )
    )
    telefone=forms.CharField(
        label='Telefone',        
        required=True,
        max_length=100,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Telefone',
                'icon': 'ph-user-circle'
            }
        )
    )
    cpf=forms.CharField(
        label='Cpf',        
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Cpf',
                'icon': 'ph-user-circle'
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
                'placeholder': '•••••••••••',
                'icon': 'ph-lock'
            }
        )
    )