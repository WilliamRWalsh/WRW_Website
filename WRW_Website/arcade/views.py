from django.shortcuts import render


def arcade(request):
    return render(request, 'arcade/index.html')


def phishing(request):
    return render(request, 'arcade/phishing.html')

