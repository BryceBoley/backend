# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='members',
            field=models.ManyToManyField(to='public.Member'),
            preserve_default=True,
        ),
    ]
