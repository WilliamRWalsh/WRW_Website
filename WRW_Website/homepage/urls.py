from django.urls import path, re_path, include
from . import views

app_name = 'homepage'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^about', views.about, name='about'),
]