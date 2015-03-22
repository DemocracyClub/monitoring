# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import screenshots.models


class Migration(migrations.Migration):

    dependencies = [
        ('url_store', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='screenshot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=screenshots.models.download_file_name)),
                ('url', models.ForeignKey(to='url_store.URL')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
