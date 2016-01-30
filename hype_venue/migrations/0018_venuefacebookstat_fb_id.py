# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hype_venue', '0017_venue_instagram_location_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='venuefacebookstat',
            name='fb_id',
            field=models.CharField(default='foobar', max_length=128),
            preserve_default=False,
        ),
    ]
