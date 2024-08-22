from django.db import models

# Create your models here.


class ContactUs(models.Model):
    subject = models.CharField(max_length=300, verbose_name='عنوان')
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    full_name = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    phone_number = models.CharField(max_length=11, verbose_name='شماره تلفن')
    message = models.TextField(verbose_name='متن تماس با ما')
    created_date = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    is_read_by_admin = models.BooleanField(default=False, verbose_name='خوانده شده توسط ادمین')

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'

    def __str__(self):
        return self.subject
