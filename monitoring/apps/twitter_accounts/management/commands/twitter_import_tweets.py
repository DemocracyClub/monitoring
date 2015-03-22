from django.core.management.base import BaseCommand

from twitter_accounts.models import TwitterUser
from twitter_accounts.tasks import get_tweets_task


class Command(BaseCommand):

    def handle(self, **options):
        for user in TwitterUser.objects.all():
            get_tweets_task.delay(user)