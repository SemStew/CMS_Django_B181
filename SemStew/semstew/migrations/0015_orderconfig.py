# Generated by Django 2.1.5 on 2019-02-12 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('semstew', '0014_language_header'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=128)),
                ('date_time', models.CharField(max_length=128)),
                ('person', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=128)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='semstew.Language')),
            ],
        ),
    ]
