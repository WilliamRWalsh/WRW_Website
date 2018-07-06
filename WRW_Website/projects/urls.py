from django.contrib import admin
from django.urls import path, re_path, include
from . import views

app_name = 'projects'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),

]
