from django.db import models

from django_extensions.db.models import TimeStampedModel

from goose import Goose

from url_store.models import URL


class Page(TimeStampedModel):
    url = models.ForeignKey(URL, max_length=800)
    page_text = models.TextField(blank=True, null=True)
    page_title = models.CharField(blank=True, max_length=800, null=True)
    title_tag = models.CharField(blank=True, max_length=800, null=True)
    raw_page = models.FileField(upload_to='raw_pages', max_length=800)


    def parse_raw(self):
        if not self.raw_page:
            return
        g = Goose()
        try:
            parsed = g.extract(raw_html=self.raw_page.read())
        except (IndexError, IOError):
            return

        h1_search = parsed.raw_doc.cssselect('h1')
        if h1_search:
            self.page_title = h1_search[0].text
            self.title_tag = parsed.title
        self.page_text = parsed.cleaned_text
        print parsed.cleaned_text
        self.save()