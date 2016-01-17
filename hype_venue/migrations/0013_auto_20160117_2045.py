# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hype_venue', '0012_auto_20160117_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='category',
            field=models.ManyToManyField(to='hype_venue.VenueCategory', null=True, blank=True),
        ),
    ]
