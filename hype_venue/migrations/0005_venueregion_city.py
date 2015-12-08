# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0004_auto_20151208_0512'),
        ('hype_venue', '0004_venue_capacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='venueregion',
            name='city',
            field=models.ForeignKey(default=1, to='cities_light.City'),
            preserve_default=False,
        ),
    ]
