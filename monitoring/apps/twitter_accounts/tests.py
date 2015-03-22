from django.test import TestCase

from .models import TwitterUser, Tweet

class TestDownloadTweets(TestCase):
    def setUp(self):
        self.no_tweet_user = TwitterUser(username='test')
        self.has_tweet_user = TwitterUser(username='symroe')
        for i in range(10):
            x = Tweet(twitter_user=self.has_tweet_user, text=i)
            x.save()

    def test_since_no_tweets(self):
        self.assertEqual(self.no_tweet_user.latest_tweet_timestamp, None)

    def test_since_with_tweets(self):
        self.assertNotEqual(self.has_tweet_user.latest_tweet_timestamp, None)

    def test_get_tweets(self):
        self.has_tweet_user.get_tweets()


