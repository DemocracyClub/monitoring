import csv
import StringIO

import requests

from django.core.management.base import BaseCommand

from twitter_accounts.models import TwitterUser

class Command(BaseCommand):

    def handle(self, **options):
        csv_url = "https://yournextmp.com/media/candidates.csv"
        req = requests.get(csv_url, verify=False)
        content = StringIO.StringIO(req.content)
        csv_data = csv.DictReader(content)
        for line in csv_data:
            if line['twitter_username']:
                user, created = TwitterUser.objects.update_or_create(
                    username=line['twitter_username'],
                    defaults={'source': 'YNMP'}
                )