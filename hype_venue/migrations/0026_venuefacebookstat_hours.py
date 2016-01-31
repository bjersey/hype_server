# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hype_venue', '0025_venueinstagramstat_tag_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='venuefacebookstat',
            name='hours',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
    ]
