from django.shortcuts import render
from places.models import Place


def show_start_page(request):
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
