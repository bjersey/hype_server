# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hype_venue', '0016_auto_20160117_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='instagram_location_id',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
    ]
