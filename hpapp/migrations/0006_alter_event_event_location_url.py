# Generated by Django 3.2.18 on 2023-04-17 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hpapp', '0005_auto_20230404_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_location_url',
            field=models.URLField(default='https://goo.gl/maps/'),
        ),
    ]
