# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('screenshots', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screenshot',
            name='url',
            field=models.ForeignKey(to='url_store.URL', max_length=800),
            preserve_default=True,
        ),
    ]
