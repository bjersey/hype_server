# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hype_venue', '0004_venue_capacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='venueregion',
            name='city',
            field=models.ForeignKey(blank=True, to='cities_light.City', null=True),
        ),
    ]
