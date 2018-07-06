from django.shortcuts import render


def index(request):
    return render(request, 'surf/index.html')


def landingpage(request):
    return render(request, 'surf/landingpage.html')


def login(request):
    return render(request, 'surf/login.html')


def simpleAnimation(request):
    return render(request, 'surf/simple_animation.html')

