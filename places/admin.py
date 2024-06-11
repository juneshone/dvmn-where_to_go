from django.contrib import admin

from places.models import Place, Imagery


class ImageryInline(admin.TabularInline):
    model = Imagery


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'description_short', 'lng', 'lat',)
    inlines = [ImageryInline]


@admin.register(Imagery)
class ImageryAdmin(admin.ModelAdmin):
    search_fields = ('place',)
    list_display = ('place', 'ordinal',)
