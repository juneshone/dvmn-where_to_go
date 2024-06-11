from django.shortcuts import render
from places.models import Place
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse


def index(request):
    places = {
      "type": "FeatureCollection",
      "features": [
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [place.lng, place.lat]
          },
          "properties": {
            "title": place.title,
            "placeId": place.id,
            "detailsUrl": reverse("places", args=(place.id,))
          }
        } for place in Place.objects.all()
      ]
    }
    return render(request, 'index.html', context={"places": places})


def upload_place_detail(request, id):
    place = get_object_or_404(Place, id=id)
    response = {
        "title": place.title,
        "imgs": [imagery.image.url for imagery in place.imageries.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.lat,
            "lng": place.lng
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
