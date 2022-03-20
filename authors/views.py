from rest_framework.viewsets import ModelViewSet
from .models import Author, Book
from .serializers import AuthorModelSerializer, BookModelSerializer


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
