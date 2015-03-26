import json

import requests
from django.core.management.base import BaseCommand
from django.conf import settings

from twitter_accounts.models import Tweet


class Command(BaseCommand):

    def handle(self, **options):

        tweets_count = Tweet.objects.all().count()

        url = "https://democlub-dashboard.herokuapp.com/widgets/tweets_archived"
        data = {
            'auth_token': settings.DASHBOARD_AUTH_TOKEN,
            'current': tweets_count,
        }
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        requests.post(url, data=json.dumps(data), headers=headers)