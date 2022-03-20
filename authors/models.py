from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()


class Book(models.Model):
    authors = models.ManyToManyField(Author)
    title = models.CharField(max_length=255)
