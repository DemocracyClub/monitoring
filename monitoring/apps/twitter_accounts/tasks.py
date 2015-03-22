from __future__ import absolute_import

from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)



@shared_task(rate_limit='15/m', default_retry_delay=900, max_retries=None)
def get_tweets_task(twitter_user):
    twitter_user.get_tweets()
