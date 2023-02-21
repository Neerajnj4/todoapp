from django.db import models


# Create your models here.

class login(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)


class register(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    email = models.EmailField(max_length=300)
    age = models.IntegerField(default=1, blank=True, null=True)

class Tasks(models.Model):
    description = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=200, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
