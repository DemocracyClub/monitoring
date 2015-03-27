from django.core.management.base import BaseCommand

from url_store.models import URL
from screenshots.tasks import screenshot_task


class Command(BaseCommand):

    def handle(self, **options):
        for url in URL.objects.all():
            screenshot_task.delay(url)
