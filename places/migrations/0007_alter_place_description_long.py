# Generated by Django 4.2.13 on 2024-06-11 16:58

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_alter_imagery_options_alter_imagery_ordinal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(verbose_name='Полное описание'),
        ),
    ]