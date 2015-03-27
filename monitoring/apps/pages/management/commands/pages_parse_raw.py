import datetime

from django.core.management.base import BaseCommand

from pages.models import Page


class Command(BaseCommand):

    def handle(self, **options):
        # for page in Page.objects.filter(page_text='',
        #                         url__last_http_status_code=200):
        for page in Page.objects.filter(page_text=''):
            page.parse_raw()