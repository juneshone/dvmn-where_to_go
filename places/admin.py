from django.contrib import admin
from django.utils.html import format_html
from places.models import Place, Imagery
from adminsortable2.admin import SortableTabularInline, SortableAdminBase


class ImageryInline(SortableTabularInline):
    model = Imagery
    readonly_fields = ('preview',)

    def preview(self, obj):
        return format_html(
            f'<img src="{obj.image.url}" style="max-height: 200px; max-width: 300px;">'
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'description_short', 'lng', 'lat',)
    inlines = [ImageryInline]


@admin.register(Imagery)
class ImageryAdmin(admin.ModelAdmin):
    search_fields = ('place',)
    list_display = ('place', 'ordinal',)
