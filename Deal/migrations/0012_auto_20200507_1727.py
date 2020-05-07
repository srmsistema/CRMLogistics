# Generated by Django 2.2.3 on 2020-05-07 11:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Deal', '0011_auto_20200506_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locationcargo',
            name='addressFrom',
        ),
        migrations.RemoveField(
            model_name='locationcargo',
            name='addressTo',
        ),
        migrations.AddField(
            model_name='locationcargo',
            name='address',
            field=models.CharField(default='', max_length=255, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='locationcargo',
            name='sendingTimeCoordinates',
            field=models.CharField(blank=True, default=datetime.time(17, 27, 51, 368124), max_length=255, verbose_name='Время отправки координат'),
        ),
        migrations.AlterField(
            model_name='order',
            name='requirementsLoading',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Требования к погрузке'),
        ),
    ]
