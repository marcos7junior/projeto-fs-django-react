from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class List(models.Model):
    owener = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=50)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    def __str__(self):
        return self.name

