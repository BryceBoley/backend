# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0002_auto_20150205_0002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='allergies',
            new_name='messages',
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(help_text=b'Describe your event', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.TextField(help_text=b'where the event is being held'),
            preserve_default=True,
        ),
    ]
