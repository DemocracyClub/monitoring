import csv
import StringIO

import requests

from django.core.management.base import BaseCommand

from url_store.models import URL

class Command(BaseCommand):

    def handle(self, **options):
        csv_url = "https://yournextmp.com/media/candidates.csv"
        req = requests.get(csv_url, verify=False)
        content = StringIO.StringIO(req.content)
        csv_data = csv.DictReader(content)
        for line in csv_data:
            url_fields = [
                'facebook_page_url',
                'homepage_url',
                'facebook_personal_url',
                'wikipedia_url',
            ]
            for f in url_fields:
                if line[f]:
                    url, created = URL.objects.update_or_create(
                        url=line[f]
                    )