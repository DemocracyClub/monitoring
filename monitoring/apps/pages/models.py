from django.db import models

from django_extensions.db.models import TimeStampedModel

from url_store.models import URL


class Page(TimeStampedModel):
    url = models.ForeignKey(URL, max_length=800)
    page_text = models.TextField(blank=True)
    page_title = models.CharField(blank=True, max_length=255)
    title_tag = models.CharField(blank=True, max_length=100)
    raw_page = models.FileField(upload_to='raw_pages', max_length=800)
