# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hype_core', '0001_initial'),
        ('hype_venue', '0023_auto_20160131_0243'),
    ]

    operations = [
        migrations.CreateModel(
            name='VenueTwitterStat',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='hype_core.TimeStampedModel')),
                ('twitter_id', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128, null=True, blank=True)),
                ('followers_count', models.PositiveIntegerField(null=True, blank=True)),
                ('venue', models.ForeignKey(to='hype_venue.Venue')),
            ],
            bases=('hype_core.timestampedmodel',),
        ),
    ]
