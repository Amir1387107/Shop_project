from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=3000, unique=True)
    password = models.CharField(max_length=20, validators=[MinLengthValidator(8),MaxLengthValidator(20)])
    email = models.EmailField(max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
