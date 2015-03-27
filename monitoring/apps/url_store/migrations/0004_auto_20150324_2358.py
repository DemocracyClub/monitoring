# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('url_store', '0003_auto_20150324_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='domain',
            field=models.CharField(max_length=800, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='url',
            name='path',
            field=models.CharField(max_length=800, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='url',
            name='querystring',
            field=models.CharField(max_length=800, blank=True),
            preserve_default=True,
        ),
    ]
