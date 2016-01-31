# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hype_venue', '0024_venuetwitterstat'),
    ]

    operations = [
        migrations.AddField(
            model_name='venueinstagramstat',
            name='tag_count',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
