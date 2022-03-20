from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}: {self.birthday_year}'


class Book(models.Model):
    authors = models.ManyToManyField(Author)
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{[author for author in self.authors.all()]} {self.title}'
