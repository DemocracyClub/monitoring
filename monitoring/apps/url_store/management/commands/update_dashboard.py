import json

import requests
from django.core.management.base import BaseCommand
from django.conf import settings

from twitter_accounts.models import Tweet
from url_store.models import URL
from screenshots.models import Screenshot


class Command(BaseCommand):

    def post_update(self, widget_id, data):
        BASE_URL = settings.DASHBOARD_BASE_URL
        data.update({'auth_token': settings.DASHBOARD_AUTH_TOKEN})

        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        requests.post(
            BASE_URL + widget_id,
            data=json.dumps(data),
            headers=headers)

    def handle(self, **options):

        tweets_count = Tweet.objects.all().count()
        URL_count = URL.objects.all().count()
        screenshot_count = Screenshot.objects.all().count()

        self.post_update('tweets_archived', {'current': tweets_count})
        self.post_update('urls_archived', {'current': URL_count})
        self.post_update('screenshots_taken', {'current': screenshot_count})
