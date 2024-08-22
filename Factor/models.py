from django.contrib.auth import models
from django.contrib.auth.models import User
from django.db import models

# f


class SellModel(models.Model):
    buyer = models.CharField(max_length=1000, verbose_name='خریدار', blank=True, null=True)
    number = models.IntegerField(verbose_name='تعداد', blank=True, null=True)
    model = models.CharField(max_length=1000, verbose_name='مدل محصول', blank=True, null=True)
    color = models.CharField(max_length=1000, verbose_name='رنگ محصول', blank=True, null=True)
    price = models.IntegerField(verbose_name='قیمت محصول', blank=True, null=True)




    class Meta:
        verbose_name = 'فروش'
        verbose_name_plural = 'فروش ها'



