# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('username', models.CharField(max_length=100, blank=True)),
                ('user_id', models.CharField(max_length=100, blank=True)),
                ('source', models.CharField(max_length=100, blank=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FacebookPost',
            fields=[
                ('post_id', models.CharField(max_length=100, serialize=False, primary_key=True, blank=True)),
                ('raw_data', models.TextField()),
                ('message', models.TextField()),
                ('status_type', models.CharField(max_length=100, blank=True)),
                ('account', models.ForeignKey(to='facebook_feeds.FacebookAccount')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
