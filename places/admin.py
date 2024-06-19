from django.contrib import admin
from django.utils.html import format_html
from places.models import Place, Imagery
from adminsortable2.admin import SortableTabularInline, SortableAdminBase


MAX_HEIGHT = 200
MAX_WIDTH = 300


class ImageryInline(SortableTabularInline):
    model = Imagery
    readonly_fields = ('get_preview',)

    def get_preview(self, obj):
        return format_html(
            f'<img src="{obj.image.url}" style="max-height: {MAX_HEIGHT}px; max-width: {MAX_WIDTH}px;">'
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'short_description', 'lng', 'lat',)
    inlines = [ImageryInline]


@admin.register(Imagery)
class ImageryAdmin(admin.ModelAdmin):
    list_display = ('place', 'ordinal',)
