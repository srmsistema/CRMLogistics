# Generated by Django 2.2.3 on 2020-05-07 17:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Deal', '0013_auto_20200507_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationcargo',
            name='sendingTimeCoordinates',
            field=models.CharField(blank=True, default=datetime.time(23, 21, 1, 657755), max_length=255, verbose_name='Время отправки координат'),
        ),
        migrations.AlterField(
            model_name='order',
            name='dateLoading',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Дата погрузки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='dateOrderConclusion',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Дата заключения заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='dateUnloading',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Дата выгрузки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='fromOrder',
            field=models.CharField(blank=True, default=datetime.date.today, max_length=100, verbose_name='Дата начала заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='toOrder',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Дата завершения заказа'),
        ),
    ]
