# Generated by Django 4.0.6 on 2022-07-14 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inWhite', '0003_rename_user_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='owner',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Owner',
        ),
    ]
