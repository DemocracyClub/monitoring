import csv
import StringIO

import requests

from django.core.management.base import BaseCommand

from url_store.models import URL
from twitter_accounts.models import TwitterUser
from facebook_feeds.models import FacebookAccount

class Command(BaseCommand):

    def add_fb_account(self, user):
        user = FacebookAccount.from_url(user)
        print user.username


    def handle(self, **options):
        csv_url = "https://yournextmp.com/media/candidates.csv"
        req = requests.get(csv_url, verify=False)
        content = StringIO.StringIO(req.content)
        csv_data = csv.DictReader(content)
        for line in csv_data:
            if 'facebook_page_url' in line:
                self.add_fb_account(line['facebook_page_url'])
            if 'facebook_personal_url' in line:
                self.add_fb_account(line['facebook_personal_url'])


            url_fields = [
                'homepage_url',
            ]
            for f in url_fields:
                if line[f]:
                    url, created = URL.objects.update_or_create(
                        url=line[f]
                    )