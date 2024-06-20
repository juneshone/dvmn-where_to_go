from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place


def index(request):
    places = {
      'type': 'FeatureCollection',
      'features': [
        {
          'type': 'Feature',
          'geometry': {
            'type': 'Point',
            'coordinates': [place.lng, place.lat]
          },
          'properties': {
            'title': place.title,
            'placeId': place.id,
            'detailsUrl': reverse('places', args=(place.id,))
          }
        } for place in Place.objects.all()
      ]
    }
    return render(request, 'index.html', context={'places': places})


def upload_place_detail(request, place_id):
    place = get_object_or_404(Place.objects.prefetch_related('imageries'), id=place_id)
    response = {
        'title': place.title,
        'imgs': [imagery.image.url for imagery in place.imageries.all()],
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': {
            'lat': place.lat,
            'lng': place.lng
        }
    }
    return JsonResponse(
        response,
        safe=False,
        json_dumps_params={
            'ensure_ascii': False,
            'indent': 2
        }
    )
