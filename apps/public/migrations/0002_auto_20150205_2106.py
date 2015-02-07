# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={},
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='blah',
        ),
    ]
