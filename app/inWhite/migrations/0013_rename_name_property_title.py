# Generated by Django 4.0.6 on 2022-07-15 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inWhite', '0012_alter_property_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='name',
            new_name='title',
        ),
    ]
