from django.contrib.auth import models
from django.contrib.auth.models import User
from django.db import models

# f


class SellModel(models.Model):
    number = models.IntegerField(verbose_name='تعداد', blank=True, null=True)
    model = models.CharField(max_length=1000, verbose_name='مدل محصول', blank=True, null=True)
    color = models.CharField(max_length=1000, verbose_name='رنگ محصول', blank=True, null=True)
    price = models.IntegerField(verbose_name='قیمت محصول', blank=True, null=True)

    class Meta:
        verbose_name = 'فروش'
        verbose_name_plural = 'فروش ها'


class More(models.Model):
    date = models.CharField(max_length=3000, blank=True, null=True)
    buyer = models.CharField(max_length=1000, verbose_name='خریدار', blank=True, null=True)
    details = models.TextField(verbose_name='توضیحات', blank=True, null=True)
    off = models.IntegerField(verbose_name='تخفیف (ریال)', blank=True, null=True)

    class Meta:
        verbose_name = 'جزییات'
        verbose_name_plural = 'جزییات ها'


class SellModelSave(models.Model):
    number = models.IntegerField(verbose_name='تعداد', blank=True, null=True)
    model = models.CharField(max_length=1000, verbose_name='مدل محصول', blank=True, null=True)
    color = models.CharField(max_length=1000, verbose_name='رنگ محصول', blank=True, null=True)
    price = models.IntegerField(verbose_name='قیمت محصول', blank=True, null=True)

    class Meta:
        verbose_name = 'ذخیره'
        verbose_name_plural = 'ذخیره ها'


class Factors(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True, auto_created=True)
    date = models.CharField(max_length=3000, blank=True, null=True)
    buyer = models.CharField(max_length=1000, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    off = models.IntegerField(blank=True, null=True)
    productsadded = models.ManyToManyField(SellModelSave, blank=True, null=True)

    class Meta:
        verbose_name = 'فاکتور'
        verbose_name_plural = 'فاکتور ها'
