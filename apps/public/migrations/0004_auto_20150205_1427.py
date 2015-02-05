# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0003_auto_20150205_0014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='pics',
        ),
        migrations.AddField(
            model_name='event',
            name='when',
            field=models.TextField(default=datetime.datetime(2015, 2, 5, 14, 27, 43, 376547, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='messages',
            field=models.TextField(help_text=b'Messages about event', null=True, blank=True),
            preserve_default=True,
        ),
    ]
