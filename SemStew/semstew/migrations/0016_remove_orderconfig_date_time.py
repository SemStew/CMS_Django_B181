# Generated by Django 2.1.5 on 2019-02-12 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('semstew', '0015_orderconfig'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderconfig',
            name='date_time',
        ),
    ]
