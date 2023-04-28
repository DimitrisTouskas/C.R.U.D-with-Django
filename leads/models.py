from pickle import TRUE
from typing import ContextManager
from django.db import models
from django.contrib.auth.models import User


class Students (models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    dieuthinsi = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    eksamino = models.IntegerField()
    A_M = models.IntegerField()


class Blospost(models.Model):
    __tablename__ = 'blogpost'
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=2000)
    tag = models.CharField(max_length=100)
    date_posted = models.DateField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


def __init__(self, title, content, tag, user_id):
    self.title = title
    self.content = content
    self.tag = tag
    self.user_id = user_id
