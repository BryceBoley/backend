# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0002_event_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='members',
        ),
    ]
