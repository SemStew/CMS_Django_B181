# Generated by Django 2.1.4 on 2018-12-28 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('semstew', '0006_auto_20181228_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='restaurant_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='semstew.New'),
        ),
    ]