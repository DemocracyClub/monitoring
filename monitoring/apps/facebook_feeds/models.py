from urlparse import urlparse
import requests
import json

from django.db import models
from django.conf import settings

from django_extensions.db.models import TimeStampedModel


class FacebookAccount(TimeStampedModel):
    username = models.CharField(blank=True, max_length=100)
    user_id = models.CharField(blank=True, max_length=100)
    source = models.CharField(blank=True, max_length=100)

    @classmethod
    def from_url(cls, url):
        KWARGS = {}
        path = urlparse(url).path
        path = path.strip('/')
        if path.startswith('pages'):
            KWARGS['user_id'] = path.split('/')[2]
        else:
            KWARGS['username'] = path

        account, created = FacebookAccount.objects.update_or_create(
            **KWARGS
        )
        return account

    def get_posts(self):
        URL = "https://graph.facebook.com/{0}/feed/?access_token={1}".format(
            self.username,
            settings.FACEBOOK_ACCESS_TOKEN,
        )

        req = requests.get(URL)
        for post_dict in req.json()['data']:
            print json.dumps(post_dict, indent=4)
            message = ""
            if 'message' in post_dict:
                message = post_dict['message']
            if 'description' in post_dict:
                message = post_dict['description']

            post, created = FacebookPost.objects.update_or_create(
                post_id=post_dict['id'],
                account=self,
                defaults={
                    'message': message,
                    'status_type': post_dict['status_type'],
                    'raw_data': json.dumps(post_dict),
                },
            )


class FacebookPost(models.Model):
    post_id = models.CharField(blank=True, max_length=100, primary_key=True)
    account = models.ForeignKey(FacebookAccount)
    raw_data = models.TextField()
    message = models.TextField()
    status_type = models.CharField(blank=True, max_length=100)
