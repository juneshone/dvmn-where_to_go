# Generated by Django 4.2.13 on 2024-06-19 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_alter_place_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='description_long',
            new_name='long_description',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='description_short',
            new_name='short_description',
        ),
    ]
