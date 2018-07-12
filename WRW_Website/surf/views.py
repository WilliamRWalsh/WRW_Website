from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.viewsets import ModelViewSet


class BookView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# class BookListAPIView(ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookDetailAPIView(RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class AuthorListAPIView(ListAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#
#
# class AuthorDetailAPIView(RetrieveAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer


def index(request):
    return render(request, 'surf/index.html')


def landingpage(request):
    return render(request, 'surf/landingpage.html')


def login(request):
    return render(request, 'surf/login.html')


def simpleAnimation(request):
    return render(request, 'surf/simple_animation.html')






