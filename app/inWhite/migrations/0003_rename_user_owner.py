# Generated by Django 4.0.6 on 2022-07-14 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inWhite', '0002_alter_property_area'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Owner',
        ),
    ]
