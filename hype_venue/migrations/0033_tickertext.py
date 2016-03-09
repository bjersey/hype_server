# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hype_core', '0001_initial'),
        ('hype_venue', '0032_venue_short_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TickerText',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='hype_core.TimeStampedModel')),
                ('text', models.CharField(max_length=32, null=True, blank=True)),
            ],
            bases=('hype_core.timestampedmodel',),
        ),
    ]
