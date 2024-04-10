from django.shortcuts import render
from django.contrib.auth import authenticate, login as django_login
from django.http import HttpResponseRedirect


# Create your views here.


def login(request):

    if request.method == 'GET':
        return render(request, 'login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user:
        django_login(request, user)
        return HttpResponseRedirect('/feed/')
    return render(request, 'login.html')


def feed(request):
    return render(request, 'feed.html')


def post(request):
    return render(request, 'teste/post.html')
