# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(help_text=b'Describe your group', null=True, blank=True)),
                ('location', models.TextField(help_text=b'What can people put into maps to get to your house')),
                ('alergies', models.TextField(null=True, blank=True)),
                ('pics', models.ImageField(null=True, upload_to=b'photos', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
