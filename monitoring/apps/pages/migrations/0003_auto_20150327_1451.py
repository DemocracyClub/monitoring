# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20150327_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='raw_page',
            field=models.FileField(max_length=800, upload_to=b'raw_pages'),
            preserve_default=True,
        ),
    ]
