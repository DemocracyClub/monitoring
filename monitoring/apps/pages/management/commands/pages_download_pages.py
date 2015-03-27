import datetime

from django.core.management.base import BaseCommand

from url_store.models import URL
from pages.tasks import save_page_task
from screenshots.tasks import screenshot_task


class Command(BaseCommand):

    def handle(self, **options):
        hour_ago = datetime.datetime.now() - datetime.timedelta(hours=1)
        day_ago = datetime.datetime.now() - datetime.timedelta(days=1)
        week_ago = datetime.datetime.now() - datetime.timedelta(days=7)

        querysets = [
             URL.objects.filter(
                 revisit_frequency="once", last_fetched=None),
             URL.objects.filter(
                 revisit_frequency="hourly",
                 last_fetched__lt=hour_ago,
             ),
             URL.objects.filter(
                 revisit_frequency="daily",
                 last_fetched__lt=day_ago,
             ),
             URL.objects.filter(
                 revisit_frequency="weekly",
                 last_fetched__lt=week_ago,
             ),
        ]

        for qs in querysets:
            for url in qs:
                save_page_task.delay(url)
                s = Screenshot(url=url)
                s.save()
                screenshot_task.delay(s)

