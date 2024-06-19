from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        'Название',
        max_length=100,
        unique=True
    )
    short_description = models.TextField(
        'Краткое описание'
    )
    long_description = HTMLField(
        'Полное описание'
    )
    lng = models.FloatField(
        'Координаты (долгота)'
    )
    lat = models.FloatField(
        'Координаты (широта)'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место для посещения'
        verbose_name_plural = 'Места для посещения'
        ordering = ['title']


class Imagery(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='imageries',
        verbose_name='Место для посещения'
    )
    image = models.ImageField(
        'Изображение',
        upload_to='images/'
    )
    ordinal = models.PositiveIntegerField(
        'Порядковый номер',
        default=1,
        db_index=True
    )

    def __str__(self):
        return f'{self.ordinal} {self.place}'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['ordinal']
