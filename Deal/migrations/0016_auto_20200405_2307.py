# Generated by Django 3.0.2 on 2020-04-05 17:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Deal', '0015_auto_20200327_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationcargo',
            name='sendingTimeCoordinates',
            field=models.CharField(blank=True, default=datetime.time(23, 7, 52, 991889), max_length=255, verbose_name='Время отправки координат'),
        ),
    ]
