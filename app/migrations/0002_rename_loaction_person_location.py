# Generated by Django 4.0.4 on 2022-05-24 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='loaction',
            new_name='location',
        ),
    ]
