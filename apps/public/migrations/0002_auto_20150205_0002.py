# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='alergies',
        ),
        migrations.AddField(
            model_name='event',
            name='allergies',
            field=models.TextField(help_text=b'attendees allergies', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.CharField(help_text=b'Describe your group', max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 2, 5, 0, 2, 8, 251737, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='event_host',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
    ]
