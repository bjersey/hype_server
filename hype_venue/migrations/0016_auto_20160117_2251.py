# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hype_venue', '0015_auto_20160117_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venueinstagramstat',
            name='followers',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
