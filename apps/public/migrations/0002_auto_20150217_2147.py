# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to=b'photos', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='start',
            field=models.DateField(default=datetime.datetime(2015, 2, 17, 21, 47, 5, 281352)),
            preserve_default=True,
        ),
    ]
