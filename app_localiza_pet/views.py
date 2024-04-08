from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'login.html')


def feed(request):
    return render(request, 'feed.html')


def post(request):
    return render(request, 'teste/post.html')
