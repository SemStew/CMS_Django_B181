# Generated by Django 2.1.2 on 2018-11-01 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('semstew', '0002_auto_20181101_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='semstew.Restaurant'),
        ),
    ]
