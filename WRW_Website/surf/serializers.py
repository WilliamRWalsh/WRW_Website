from rest_framework.serializers import (ModelSerializer, HyperlinkedModelSerializer, HyperlinkedIdentityField, StringRelatedField, HyperlinkedRelatedField)
from .models import Book, Author


class BookSerializer(ModelSerializer):
    author = StringRelatedField()
    # author = HyperlinkedRelatedField(read_only='True', view_name='Author-detail')

    class Meta:
        model = Book
        fields = ('title', 'author')


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ('firstName', 'lastName')


