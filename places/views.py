from django.shortcuts import render
from places.models import Place
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


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
            "detailsUrl": "static/places"
          }
        } for place in Place.objects.all()
      ]
    }
    return render(request, 'index.html', context={"places": places})


def get_place(request, id):
    place = get_object_or_404(Place, id=id)
    return HttpResponse(place)
