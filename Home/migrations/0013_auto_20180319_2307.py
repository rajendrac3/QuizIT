# Generated by Django 2.0.1 on 2018-03-19 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_remove_question_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='slug',
            field=models.SlugField(blank=True, max_length=500),
        ),
    ]
