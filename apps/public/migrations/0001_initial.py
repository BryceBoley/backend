# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('start', models.DateField(default=datetime.datetime(2015, 2, 13, 22, 45, 55, 493509))),
                ('comment', models.TextField(help_text=b'comment', null=True, blank=True)),
                ('host', models.TextField(help_text=b'Who is hosting', null=True, blank=True)),
                ('when', models.TextField(max_length=10, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(default=b'N/A', max_length=15)),
                ('street', models.CharField(default=b'N/A', max_length=75)),
                ('city', models.CharField(default=b'N/A', max_length=50)),
                ('state', models.CharField(default=b'N/A', max_length=35)),
                ('food_allergies', models.TextField(default=b'Have any food allergies?', max_length=75, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
