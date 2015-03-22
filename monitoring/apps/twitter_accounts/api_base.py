from django.conf import settings

import twitter as twitter_api

api = twitter_api.Api(
    consumer_key=settings.TWITTER_KEY,
    consumer_secret=settings.TWITTER_SECRET,
    access_token_key=settings.TWITTER_TOKEN,
    access_token_secret=settings.TWITTER_TOKEN_SECRET
)