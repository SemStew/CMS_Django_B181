# Generated by Django 2.1.4 on 2018-12-28 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semstew', '0009_auto_20181228_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemname',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
