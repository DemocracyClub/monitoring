import csv
import StringIO

import requests

from django.core.management.base import BaseCommand

from url_store.models import URL

class Command(BaseCommand):

    def handle(self, **options):
        URLS = [
            "https://docs.google.com/a/democracyclub.org.uk/spreadsheets/d/1BuC-y0mxzzJs0LAwPTnELKYI76D_lX6ikmWhj6voE90/export?format=csv&id=1BuC-y0mxzzJs0LAwPTnELKYI76D_lX6ikmWhj6voE90&gid=0"
        ]

        for CSV_URL in URLS:
            req = requests.get(CSV_URL, verify=False)
            content = StringIO.StringIO(req.content)
            csv_data = csv.reader(content)
            for line in csv_data:
                url, created = URL.objects.update_or_create(
                    url=line[0],
                    revisit_frequency=line[1],
                )