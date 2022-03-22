from django.db import models

# https://stackoverflow.com/questions/30471700/storing-list-of-objects-in-django-model
# https://stackoverflow.com/questions/30765360/how-to-deserialize-nested-objects-with-django-rest-framework


class Kid(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.first_name} {self.last_name}: {self.birthday_year}'


class Sleep(models.Model):
    kid = models.ForeignKey(Kid, on_delete=models.CASCADE)
    date = models.DateTimeField()

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.kid} {self.date}'
