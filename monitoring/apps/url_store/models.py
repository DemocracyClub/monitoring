import requests

from urlparse import urlparse, parse_qs
import urllib

from django.db import models
from django.core.files.base import ContentFile
from django.utils.text import slugify

from django_extensions.db.models import TimeStampedModel

from .managers import URLManager

DOWNLOAD_FREQUENCIES = (
    ("once", "Once"),
    ("hourly", "Hourly"),
    ("daily", "Daily"),
    ("weekly", "Weekly"),
)


class URL(TimeStampedModel):
    url = models.URLField(max_length=800, blank=False, null=False)
    domain = models.CharField(blank=True, max_length=800)
    path = models.CharField(blank=True, max_length=800)
    querystring = models.CharField(blank=True, max_length=800)
    last_fetched = models.DateTimeField(blank=True, null=True)
    last_http_status_code = models.IntegerField(blank=True, null=True)
    revisit_frequency = models.CharField(
        blank=True, max_length=100, choices=DOWNLOAD_FREQUENCIES)

    objects = URLManager()

    @property
    def base_date(self):
        """
        Currently only support daily or one off fetching
        """
        return self.modified.date().isoformat()

    def base_file_name(self):
        """
        There is a need to have a predictable file name.  This should be used
        everywhere URLs in some form are saved to disk.
        """
        # Call this just incase the propties haven't been set yet.
        self.url_to_parts()
        file_name = "-".join([
                self.base_date,
                self.domain,
                self.path,
                self.querystring,
        ])
        file_name = file_name.replace('/', '-').lower()
        file_name = file_name.replace('=', '-').lower()
        file_name = file_name.replace('--', '-')
        return file_name.strip('/-')

    def url_to_parts(self):
        parsed_url = urlparse(self.url)
        self.domain = parsed_url.hostname
        self.path = parsed_url.path
        query_tmp = parse_qs(parsed_url.query)

        for k,v in query_tmp.items():
            if k.startswith('utm_'):
                del query_tmp[k]
        flattened_qs = [
            (k,v) for k,vlist in query_tmp.iteritems() for v in vlist]
        self.querystring = urllib.urlencode(flattened_qs)

    def save(self, *args, **kwargs):
        self.url_to_parts()
        if not self.revisit_frequency:
            self.revisit_frequency = "once"

        return super(URL, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.url


def download_file_name(instance, filename):
    return "/".join([
        "downloaded_urls",
        instance.base_file_name,
        str(instance.pk)
    ])


class URLDownload(TimeStampedModel):
    url = models.ForeignKey(URL)
    downloaded_file = models.FileField(upload_to=download_file_name)

    def download(self):
        self.save()
        res = requests.get(self.url.url, verify=False)
        # import ipdb; ipdb.set_trace()
        self.downloaded_file.save(self.pk, ContentFile(res.text))

