# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hype_venue', '0014_venuefacebookstat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='category',
            field=models.ManyToManyField(to='hype_venue.VenueCategory', blank=True),
        ),
    ]
