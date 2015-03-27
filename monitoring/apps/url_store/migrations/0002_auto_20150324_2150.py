# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('url_store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='revisit_frequency',
            field=models.CharField(blank=True, max_length=100, choices=[(b'once', b'Once'), (b'daily', b'Daily')]),
            preserve_default=True,
        ),
    ]
