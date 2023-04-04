# Generated by Django 3.2.18 on 2023-04-04 09:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hpapp', '0004_delete_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_time',
            field=models.TimeField(default=datetime.time(8, 0)),
        ),
        migrations.AddField(
            model_name='event',
            name='event_time_reg_close',
            field=models.TimeField(default=datetime.time(23, 59)),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date_reg_close',
            field=models.DateField(),
        ),
    ]
