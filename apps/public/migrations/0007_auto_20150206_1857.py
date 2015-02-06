# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0006_auto_20150206_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='members',
            field=models.CharField(max_length=250, null=True),
            preserve_default=True,
        ),
    ]
