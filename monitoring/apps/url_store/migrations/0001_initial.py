# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import url_store.models
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('url', models.URLField()),
                ('domain', models.CharField(max_length=255, blank=True)),
                ('path', models.CharField(max_length=255, blank=True)),
                ('querystring', models.CharField(max_length=255, blank=True)),
                ('last_fetched', models.DateTimeField(null=True, blank=True)),
                ('last_http_status_code', models.IntegerField(null=True, blank=True)),
                ('revisit_frequency', models.CharField(blank=True, max_length=100, choices=[(b'daily', b'Daily')])),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='URLDownload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('downloaded_file', models.FileField(upload_to=url_store.models.download_file_name)),
                ('url', models.ForeignKey(to='url_store.URL')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
    ]
