from django.contrib import admin

from places.models import Place, Imagery


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'description_short', 'lng', 'lat',)


@admin.register(Imagery)
class ImageryAdmin(admin.ModelAdmin):
    search_fields = ('place',)
    list_display = ('place', 'ordinal',)
