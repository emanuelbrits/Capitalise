# Create your views here.
from django.shortcuts import render, redirect
from cadastro.forms import CadastroForms
# from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib import messages
from ..app.models import Usuario
from .forms import CadastroForms

def cadastro(request):
    if request.method == 'GET':
        print(f'Início método GET')
        id = request.GET.get('id')
        if id:
            obj = Usuario.objects.get(id=id)
            form = CadastroForms(initial=obj.__dict__)
        else:
            form = CadastroForms()

        args = {}               
        args = {
            'menuselecionado': 'cadastro',
            'form': form,
            'id': id        
        }    
        return render(request, 'cadastro/cadastro.html', args) 
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            nome = form['nome'].value()
            cpf = form['cpf'].value()
            email = form['email'].value()
            telefone = form['telefone'].value()
            senha = form['senha'].value()
        
        usuario_novo = Usuario.objects.create(
                    nome=nom_usr,
                    cpf=num_cpf,
                    email=end_email,
                    telefone=num_telefone,
                    senha=pass_senha
                )
        
    return render(request, 'autenticacao/login .html', {'form': form})
