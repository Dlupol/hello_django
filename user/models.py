from django.contrib.auth.models import AbstractUser
from django.db import models


class Permission(models.Model):

    name = models.CharField(max_length=200)


class Role(models.Model):

    name = models.CharField(max_length=200)
    permissions = models.ManyToManyField(Permission)


class Users(AbstractUser):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=200)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
