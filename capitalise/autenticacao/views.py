# Create your views here.
from django.shortcuts import render, redirect
from autenticacao.forms import LoginForms, CadastroForms
# from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
#from ..app.models import Usuario

def cadastro(request):
    form = CadastroForms()

    # if request.method == 'POST':
    #     form = CadastroForms(request.POST)

    #     if form.is_valid():
    #         email = form['email'].value()
    #         nome = form['nome'].value()
    #         telefone = form['telefone'].value()
    #         cpf = form['cpf'].value()
    #         senha = form['senha'].value()
    #         User.objects.create_user(nome, email, senha)
    #         Usuario.objects.create(
    #                     nom_usr=nome,
    #                     num_cpf=cpf,
    #                     num_telefone=telefone,
    #                     end_email=email,
    #                     senha=senha,
    #                 )

    return render(request, 'autenticacao/cadastro.html', {'form': form})

def login(request):
    form = LoginForms()      

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            login = form['usuario'].value()
            senha = form['senha'].value()
        
        usuario = auth.authenticate(
            request,
            username=login,
            password=senha
        )
        if usuario is not None:
            auth.login(request, usuario)
            #messages.success(request, f'{login} logado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha inválidos!')
            return redirect('login')

    return render(request, 'autenticacao/login.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('login')