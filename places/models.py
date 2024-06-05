from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=100)
    description_short = models.TextField(
        'Краткое описание'
    )
    description_long = models.TextField(
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
