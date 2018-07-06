from django.contrib import admin
from django.urls import path, re_path, include
from . import views

app_name = 'arcade'

urlpatterns = [
    re_path(r'^phishing$', views.phishing, name='phishing'),
    re_path(r'^$', views.arcade, name='index'),
]
