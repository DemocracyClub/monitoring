import time
import json

from django.db import models

from django_extensions.db.models import TimeStampedModel

from .api_base import api

class TwitterUser(TimeStampedModel):
    username = models.CharField(blank=True, max_length=100, primary_key=True)
    source = models.CharField(blank=True, max_length=100)

    @property
    def latest_tweet(self):
        try:
            return self.tweet_set.latest('tweet_id')
        except Tweet.DoesNotExist:
            return None


    @property
    def latest_tweet_timestamp(self):
        if self.latest_tweet:
            return time.mktime(self.latest_tweet.created.timetuple())

    def get_tweets(self):

        latest_tweet = self.latest_tweet
        kwargs = {
            'screen_name': self.username
        }
        if latest_tweet:
            kwargs['since_id'] = latest_tweet.pk
        statuses = api.GetUserTimeline(**kwargs)
        for tweet in statuses:
            tweet_obj, created = Tweet.objects.update_or_create(
                tweet_id=tweet.id,
                raw_data=json.dumps(tweet.AsDict()),
                twitter_user=self,
                text=tweet.text,
            )

class Tweet(TimeStampedModel):
    tweet_id = models.CharField(blank=True, max_length=100, primary_key=True)
    raw_data = models.TextField()
    twitter_user = models.ForeignKey(TwitterUser)
    text = models.CharField(blank=True, max_length=200)
