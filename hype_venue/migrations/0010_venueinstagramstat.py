# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hype_core', '0001_initial'),
        ('hype_venue', '0009_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='VenueInstagramStat',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='hype_core.TimeStampedModel')),
                ('followers', models.IntegerField()),
                ('venue', models.ForeignKey(to='hype_venue.Venue')),
            ],
            bases=('hype_core.timestampedmodel',),
        ),
    ]
