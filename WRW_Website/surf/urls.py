from django.contrib import admin
from django.urls import path, re_path, include
from . import views

app_name = 'surf'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^landingpage', views.landingpage, name='landingpage'),
    re_path(r'^login', views.login, name='login'),
    re_path(r'^simple_animation', views.simpleAnimation, name='simpleAnimation'),
]
