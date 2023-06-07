# Create your views here.
from django.shortcuts import render, redirect
from autenticacao.forms import LoginForms
# from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

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