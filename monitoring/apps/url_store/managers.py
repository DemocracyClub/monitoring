import datetime

from django.db import models


class URLQuerySet(models.QuerySet):
    def since(self, delta):
        now = datetime.datetime.now()
        time_since = now - delta
        return self.filter(last_fetched__lt=time_since)

    def editors(self):
        return self.filter(role='E')

class URLManager(models.Manager):
    def get_queryset(self):
        return URLQuerySet(self.model, using=self._db)

    def hour_ago(self):
        return self.get_queryset().since(datetime.timedelta(hours=1))

    def day_ago(self):
        return self.get_queryset().since(datetime.timedelta(days=1))

    def week_ago(self):
        return self.get_queryset().since(datetime.timedelta(days=7))

    def since(self, delta):
        return self.get_queryset().since(delta)


