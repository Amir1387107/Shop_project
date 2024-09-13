from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Product(models.Model):
    user = models.CharField(max_length=10000000)
    price = models.CharField(max_length=300, verbose_name='قیمت')
    model = models.CharField(max_length=300, verbose_name='مدل')
    color = models.CharField(max_length=300, verbose_name='رنگ')
    kind = models.CharField(max_length=3000)
    details = models.TextField(verbose_name='توضیحات', blank=True, null=True)

