# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields.hstore


class Migration(migrations.Migration):

    dependencies = [
        ('hype_core', '0001_initial'),
        ('hype_venue', '0027_auto_20160131_0613'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScoreParameters',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='hype_core.TimeStampedModel')),
                ('name', models.CharField(max_length=32)),
                ('data', django.contrib.postgres.fields.hstore.HStoreField(null=True, blank=True)),
            ],
            bases=('hype_core.timestampedmodel',),
        ),
    ]
