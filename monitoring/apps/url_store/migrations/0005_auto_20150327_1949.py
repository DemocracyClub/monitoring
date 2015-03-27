# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('url_store', '0004_auto_20150324_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='revisit_frequency',
            field=models.CharField(blank=True, max_length=100, choices=[(b'once', b'Once'), (b'hourly', b'Hourly'), (b'daily', b'Daily'), (b'weekly', b'Weekly')]),
            preserve_default=True,
        ),
    ]
