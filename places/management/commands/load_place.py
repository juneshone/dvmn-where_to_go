import requests
import time

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from requests.exceptions import HTTPError, ConnectionError

from places.models import Place, Imagery


class Command(BaseCommand):
    help = 'Download place in format json in DB'

    def add_arguments(self, parser):
        parser.add_argument(
            '--json_url',
            type=str,
            help='Json url',
        )

    def load_place(self, response):
        raw_place = response.json()
        place = Place.objects.get_or_create(
            title=raw_place['title'],
            defaults={
                'short_description': raw_place['description_short'],
                'long_description': raw_place['description_long'],
                'lng': raw_place['coordinates']['lng'],
                'lat': raw_place['coordinates']['lat'],
            }
        )

        for ordinal, image_url in enumerate(raw_place['imgs'], 1):
            if image_url:
                response = requests.get(image_url)
                response.raise_for_status()
                Imagery.objects.get_or_create(
                    place=place[0],
                    image=ContentFile(response.content, image_url.split('/')[-1]),
                    ordinal=ordinal,
                )

    def handle(self, *args, **options):
        try:
            json_url = options['json_url']
            if json_url:
                response = requests.get(json_url)
                response.raise_for_status()
                if response.ok:
                    self.load_place(response)
        except HTTPError as e:
            print(f'{type(e)}:Ссылка не найдена.')
        except ConnectionError as e:
            print(f'{type(e)}:Проблемы соединения. Повторная попытка.')
            time.sleep(10)
