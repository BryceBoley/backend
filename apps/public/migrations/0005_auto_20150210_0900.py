# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0004_auto_20150210_0728'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='city',
            field=models.CharField(default=b'N/A', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='food_allergies',
            field=models.TextField(default=b'Have any food allergies?', max_length=75, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='phone_number',
            field=models.CharField(default=b'N/A', max_length=15),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='state',
            field=models.CharField(default=b'N/A', max_length=35),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='street',
            field=models.CharField(default=b'N/A', max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='when',
            field=models.TextField(help_text=b'When event is to take place'),
            preserve_default=True,
        ),
    ]
