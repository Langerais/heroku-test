# Generated by Django 4.0.6 on 2022-07-14 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inWhite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='area',
            field=models.IntegerField(),
        ),
    ]
