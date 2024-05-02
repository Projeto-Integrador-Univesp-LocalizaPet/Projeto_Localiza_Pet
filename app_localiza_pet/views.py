from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import MyFile
import random


# Create your views here.

def entrada(request):
    return redirect('/login/')


def login(request):

    if request.method == 'GET':
        return render(request, 'login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user:
        django_login(request, user)
        return HttpResponseRedirect('/feed/')
    msg = 'Usuario e(ou) senha invalidos'
    return render(request, 'login.html', {'msg': msg})


@login_required(login_url='/login/')
def feed(request):
    return render(request, 'novo_feed.html')


@login_required(login_url='/login/')
def post(request):
    if request.method == 'GET':
        return render(request, 'post.html')
    elif request.method == 'POST':  # retorna os arquivos da pagina
        file = {}
        file.update(request.FILES)
        # Salva em uma lista os arquivos retornados pelo metodo POST
        ret = file["my_file"]
        name = ''
        for i in '0123456789':  # cria um numero unico para a postagem
            name += str(random.randint(0, 9))
        for i in ret:  # Salva no banco todos os arquivos com o numero unico da postagem
            mf = MyFile(title=name, arq=i)
            mf.save()
    return HttpResponseRedirect('/feed/')


@login_required(login_url='/login/')
def logout(request):
    django_logout(request)
    return redirect('/login/')


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)
    if user:
        return redirect('/login/')

    User.objects.create_user(
        username=request.POST.get('username'),
        password=request.POST.get('password'),
    )
    return render(request, 'login.html')
