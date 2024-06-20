from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from places import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('places/<int:place_id>/', views.upload_place_detail, name='places'),
    path('', views.index, name='index'),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
