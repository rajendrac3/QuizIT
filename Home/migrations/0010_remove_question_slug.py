# Generated by Django 2.0.1 on 2018-03-18 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_auto_20180318_1854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='slug',
        ),
    ]
