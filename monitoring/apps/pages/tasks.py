import datetime

import requests
from celery import shared_task

from django.core.files.base import ContentFile
from django.template.defaultfilters import slugify

from pages.models import Page

@shared_task
def save_page_task(url):
    page = Page(url=url)
    page.save()
    try:
        req = requests.get(url.url)
    except requests.exceptions.ConnectionError:
        url.last_fetched = datetime.datetime.now()
        url.last_http_status_code = 503
        url.save()
        return

    file_name = slugify("-".join([str(url.pk), url.domain, url.path]))[:50]

    page.raw_page.save(file_name, ContentFile(req.text))
    page.save()
    url.last_fetched = datetime.datetime.now()
    url.last_http_status_code = req.status_code
    url.save()
