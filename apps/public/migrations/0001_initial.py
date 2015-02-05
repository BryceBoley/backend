# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(help_text=b'Describe your group', blank=True)),
                ('location', models.TextField(help_text=b'Where should members go for your dinner group?')),
                ('food_allergies', models.TextField(blank=True)),
                ('pics', models.ImageField(null=True, upload_to=b'photos', blank=True)),
                ('host', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('blah', models.CharField(max_length=15)),
                ('street', models.CharField(max_length=75)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=35)),
                ('food_allergies', models.TextField(default=b'Have any food allergies you want the group to know about?', max_length=75, blank=True)),
                ('profile_picture', models.ImageField(null=True, upload_to=b'photos', blank=True)),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
    ]
