from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(max_length=32, unique=True)
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return f"{self.username} - {self.email}"