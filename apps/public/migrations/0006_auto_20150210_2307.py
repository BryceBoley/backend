# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0005_auto_20150210_0900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='event',
            name='when',
        ),
        migrations.AddField(
            model_name='event',
            name='alergies',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(default='string', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='pics',
            field=models.ImageField(null=True, upload_to=b'photos', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(help_text=b'Describe your group', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.TextField(help_text=b'What can people put into maps to get to your house'),
            preserve_default=True,
        ),
    ]
