# Generated by Django 4.2.13 on 2024-06-11 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_alter_imagery_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagery',
            options={'ordering': ['ordinal'], 'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
        migrations.AlterField(
            model_name='imagery',
            name='ordinal',
            field=models.PositiveIntegerField(db_index=True, default=1, verbose_name='Порядковый номер'),
        ),
    ]
