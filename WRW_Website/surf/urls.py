from django.urls import path, re_path, include
from rest_framework import routers
from rest_framework import generics
from . import views


app_name = 'surf'
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'books', views.BookView)
router.register(r'authors', views.AuthorView)

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^landingpage', views.landingpage, name='landingpage'),
    re_path(r'^login', views.login, name='login'),
    re_path(r'^simple_animation', views.simpleAnimation, name='simpleAnimation'),
    # re_path(r'^api/', include('surf.api.urls')),
    re_path(r'^api/', include(router.urls), name='api'),




    # re_path(r'^api/$', views.BookListAPIView.as_view(), name='book-list'),
    # re_path(r'^api/(?P<pk>\d+)/', views.BookDetailAPIView.as_view(), name='book-detail'),
    # re_path(r'^api/author/$', views.AuthorListAPIView.as_view(), name='author-list'),
    # re_path(r'^api/author/(?P<pk>\d+)/', views.AuthorDetailAPIView.as_view(), name='author-detail'),

]
