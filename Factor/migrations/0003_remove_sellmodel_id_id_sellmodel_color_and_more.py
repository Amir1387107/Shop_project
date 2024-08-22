# Generated by Django 5.0.7 on 2024-08-20 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Factor', '0002_remove_sellmodel_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellmodel',
            name='id_id',
        ),
        migrations.AddField(
            model_name='sellmodel',
            name='color',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='رنگ محصول'),
        ),
        migrations.AddField(
            model_name='sellmodel',
            name='model',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='مدل محصول'),
        ),
        migrations.AddField(
            model_name='sellmodel',
            name='number',
            field=models.IntegerField(blank=True, null=True, verbose_name='تعداد'),
        ),
        migrations.AddField(
            model_name='sellmodel',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='قیمت محصول'),
        ),
        migrations.AlterField(
            model_name='sellmodel',
            name='buyer',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='خریدار'),
        ),
    ]
