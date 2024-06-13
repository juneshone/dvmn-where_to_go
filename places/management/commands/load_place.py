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
        place = Place.objects.get_or_create(
            title=response.json()['title'],
            defaults={
                'description_short': response.json()['description_short'],
                'description_long': response.json()['description_long'],
                'lng': response.json()['coordinates']['lng'],
                'lat': response.json()['coordinates']['lat'],
            }
        )

        for ordinal, image_url in enumerate(response.json()['imgs'], 1):
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
                if response.status_code == 200:
                    self.load_place(response)
        except HTTPError as e:
            print(f'{type(e)}:Ссылка не найдена.')
        except ConnectionError as e:
            print(f'{type(e)}:Проблемы соединения. Повторная попытка.')
            time.sleep(10)
