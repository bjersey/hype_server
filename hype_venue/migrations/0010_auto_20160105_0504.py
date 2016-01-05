# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


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
            ],
            bases=('hype_core.timestampedmodel',),
        ),
        migrations.RemoveField(
            model_name='venue',
            name='id',
        ),
        migrations.RemoveField(
            model_name='venueregion',
            name='id',
        ),
        migrations.AddField(
            model_name='venue',
            name='timestampedmodel_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=datetime.datetime(2016, 1, 5, 5, 3, 51, 357854, tzinfo=utc), serialize=False, to='hype_core.TimeStampedModel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venueregion',
            name='timestampedmodel_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=datetime.datetime(2016, 1, 5, 5, 4, 1, 782241, tzinfo=utc), serialize=False, to='hype_core.TimeStampedModel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venueinstagramstat',
            name='venue',
            field=models.ForeignKey(to='hype_venue.Venue'),
        ),
    ]
