# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hype_core', '0001_initial'),
        ('hype_venue', '0013_auto_20160117_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='VenueFacebookStat',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='hype_core.TimeStampedModel')),
                ('likes', models.IntegerField(null=True, blank=True)),
                ('category', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=256, null=True, blank=True), blank=True)),
                ('venue', models.ForeignKey(to='hype_venue.Venue')),
            ],
            bases=('hype_core.timestampedmodel',),
        ),
    ]
