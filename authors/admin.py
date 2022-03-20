from django.contrib import admin

from authors.models import Author, Book

admin.site.register(Author)
admin.site.register(Book)
