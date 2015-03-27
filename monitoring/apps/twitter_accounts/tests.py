import json

from django.test import TestCase

from .models import TwitterUser, Tweet

RAW_TWEET = json.dumps({"lang": "en", "favorited": False, "truncated": False, "text": "http://t.co/Tc0lBQkM backs Green Party for Birmingham. Respect for Greens!", "created_at": "Fri Apr 20 14:50:55 +0000 2012", "retweeted": False, "source": "<a href=\"https://about.twitter.com/products/tweetdeck\" rel=\"nofollow\">TweetDeck</a>", "user": {"lang": "en", "profile_background_tile": False, "statuses_count": 56, "screen_name": "HarborneGreen", "friends_count": 16, "profile_link_color": "0084B4", "created_at": "Wed Apr 14 17:43:41 +0000 2010", "profile_sidebar_fill_color": "DDEEF6", "profile_image_url": "https://pbs.twimg.com/profile_images/841181162/Phil_Simpson1_normal.jpg", "profile_text_color": "333333", "followers_count": 43, "protected": False, "profile_background_color": "C0DEED", "listed_count": 13, "id": 132975920, "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png", "name": "Phil Simpson"}, "urls": {"http://t.co/Tc0lBQkM": "http://Salmayaqoob.com"}, "id": 193351043059417088})



class TestDownloadTweets(TestCase):
    def setUp(self):
        self.no_tweet_user = TwitterUser(username='test')
        self.has_tweet_user = TwitterUser(username='symroe')
        for i in range(10):
            x = Tweet(
                twitter_user=self.has_tweet_user,
                text=i,
                raw_data=RAW_TWEET)
            x.save()

    def test_since_no_tweets(self):
        self.assertEqual(self.no_tweet_user.latest_tweet_timestamp, None)

    def test_since_with_tweets(self):
        self.assertNotEqual(self.has_tweet_user.latest_tweet_timestamp, None)

    def test_get_tweets(self):
        self.has_tweet_user.get_tweets()

    def test_parse_urls(self):

        self.assertEqual(Tweet.objects.all()[0].parse_urls(),
            set([u'http://Salmayaqoob.com']))
