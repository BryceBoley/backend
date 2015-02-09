# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='food_allergies',
            new_name='comments',
        ),
        migrations.RemoveField(
            model_name='event',
            name='pics',
        ),
        migrations.AddField(
            model_name='event',
            name='members',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='when',
            field=models.TextField(help_text=b'Where event is to take place', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
