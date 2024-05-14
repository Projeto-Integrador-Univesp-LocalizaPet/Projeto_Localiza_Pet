from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Animal_post
import random


# Create your views here.

def entrada(request):
    return redirect('/feed/')


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


def feed(request):
    animais_postados = Animal_post.objects.all()
    return render(request, 'novo_feed.html', {
        'animais_postados': animais_postados,
    })


def post_pet(request, post_id):
    pet = Animal_post.objects.get(id=post_id)
    return render(request, 'post_pet.html', {
        'pet': pet,
    })


@login_required(login_url='/login/')  # Pagina para postar revisada OK
def publicar(request):
    if request.method == 'GET':
        return render(request, 'publicar.html')
    elif request.method == 'POST':  # retorna os arquivos da pagina
        # retorna as imagens da postagem
        formulario = {}
        formulario.update(request.FILES)
        retorno = formulario['my_file']
        # Adiciona um serial para todas as fotos do mesmo post
        serial = ''
        # retorna descrição, situação e usuario do post
        username = request.user
        descricao = request.POST.get('desc')
        situ = request.POST.get('situação')
        for i in '0123456789':  # cria um numero unico para a postagem
            serial += str(random.randint(0, 9))
        for i in retorno:  # Salva o post no banco de dados
            dado = Animal_post(serial=serial, foto=i, descricao=descricao, opcao=situ,
                               user=username)
            dado.save()
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
