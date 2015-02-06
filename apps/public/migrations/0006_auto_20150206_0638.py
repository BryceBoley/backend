# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0005_auto_20150205_2201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('event_host', models.CharField(max_length=100, null=True)),
                ('location', models.TextField(help_text=b'where the event is being held')),
                ('when', models.TextField(max_length=100)),
                ('description', models.TextField(help_text=b'Describe your event', null=True, blank=True)),
                ('messages', models.TextField(help_text=b'Messages about event', null=True, blank=True)),
                ('members', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Dinner',
        ),
    ]
