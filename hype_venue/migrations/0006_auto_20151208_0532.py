# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hype_venue', '0005_venueregion_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venueregion',
            name='city',
            field=models.ForeignKey(default=1, to='cities_light.City'),
            preserve_default=False,
        ),
    ]
