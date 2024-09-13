from typing import Any, Iterable
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import datetime
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator

now = datetime.date.today()
now_month=str(now.month)
now_day=str(now.day)
now_year=str(now.year)



class Debts(models.Model):
    creditor = models.CharField(max_length=500, verbose_name='طلبکار')
    amount_of_debt = models.IntegerField(verbose_name='مقدار بدهی (ریال)')
    payment_deadline = models.DateField(verbose_name='(به میلادی)مهلت پرداخت', auto_now=False,auto_now_add=False)


    def __str__(self):
        return self.creditor


    class Meta:
        verbose_name='بدهی'
        verbose_name_plural='بدهی ها'
                

class Requests(models.Model):
    debtor = models.CharField(max_length=500, verbose_name='بدهکار')
    amount_of_debt = models.IntegerField(verbose_name='مقدار طلب (ریال)')
    payment_deadline = models.DateField(verbose_name='(به میلادی)مهلت پرداخت', auto_now=False,auto_now_add=False)

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    def __str__(self):
        return self.debtor


    class Meta:
        verbose_name='بستانکار'
        verbose_name_plural='بستانکار ها'
    


class Kind(models.Model):
    kind = models.CharField(max_length=300, verbose_name='دسته')

    def __str__(self):
        return self.kind

    class Meta:
        verbose_name = 'دسته'
        verbose_name_plural = 'دسته بندی'


class reviews(models.Model):
    username = models.CharField(max_length=1000, verbose_name='نام کاربری')
    product_id = models.IntegerField(verbose_name='id محصول')
    review = models.TextField(verbose_name='نظر')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'


class Products(models.Model):
    price = models.CharField(max_length=300, verbose_name='قیمت')
    model = models.CharField(max_length=300, verbose_name='مدل')
    color = models.CharField(max_length=300, verbose_name='رنگ')
    kind = models.ManyToManyField(Kind, related_name='Kind', verbose_name='دسته')
    details = models.TextField(verbose_name='توضیحات', blank=True, null=True)

    image1 = models.ImageField(upload_to='Images/', verbose_name='عکس1', blank=True)
    image2 = models.ImageField(upload_to='Images/', verbose_name='عکس2', blank=True)
    image3 = models.ImageField(upload_to='Images/', verbose_name='عکس3', blank=True)
    image4 = models.ImageField(upload_to='Images/', verbose_name='عکس4', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify((self.id))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.model

    class Meta: 
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
    

class Orders(models.Model):
    product_model = models.CharField(max_length=300000, verbose_name='اسم محصول', null=True, blank=True)
    product_color = models.CharField(max_length=300000, verbose_name='رنگ محصول', null=True, blank=True)
    Buyer = models.CharField(max_length=200, verbose_name='نام و نام خانوادگی خریدار')
    Phone_one = models.CharField(max_length=300, verbose_name='شماره همراه اول')
    Phone_two = models.CharField(max_length=300, verbose_name='شماره همراه دوم')
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    Address = models.CharField(max_length=100000, verbose_name='آدرس')

    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.product_model

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'
    

class UserOfSite(models.Model):
    username = models.CharField(max_length=3000, unique=True)
    password = models.CharField(max_length=20, validators=[MinLengthValidator(8), MaxLengthValidator(20)])
    phone_number = models.CharField(max_length=11, validators=[RegexValidator(r'^\d{11}$')], unique=True)
    email = models.EmailField(max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
