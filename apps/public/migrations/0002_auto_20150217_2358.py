# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start',
            field=models.DateField(default=datetime.datetime(2015, 2, 17, 23, 58, 28, 157486)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='apartment_number',
            field=models.CharField(default=b'', max_length=25, blank=True),
            preserve_default=True,
        ),
    ]
