from rest_framework.serializers import ModelSerializer

from .models import Author, Book


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookModelSerializer(ModelSerializer):
    authors = AuthorModelSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'
