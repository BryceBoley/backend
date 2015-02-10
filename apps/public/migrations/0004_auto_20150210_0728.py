# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0003_remove_event_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='host',
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.TextField(help_text=b'Where should members go for your dinner group?', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='when',
            field=models.TextField(help_text=b'When event is to take place', blank=True),
            preserve_default=True,
        ),
    ]
