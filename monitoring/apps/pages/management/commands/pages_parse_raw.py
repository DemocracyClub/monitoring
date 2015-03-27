import datetime

from django.core.management.base import BaseCommand

from pages.tasks import parse_page_task


class Command(BaseCommand):

    def handle(self, **options):
        for page in Page.objects.filter(page_text='',
                                url__last_http_status_code=200):
            parse_page_task.delay(page)