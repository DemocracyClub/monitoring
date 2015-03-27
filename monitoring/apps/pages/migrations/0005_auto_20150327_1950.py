# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20150327_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='page_title',
            field=models.CharField(max_length=800, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='title_tag',
            field=models.CharField(max_length=800, null=True, blank=True),
            preserve_default=True,
        ),
    ]
