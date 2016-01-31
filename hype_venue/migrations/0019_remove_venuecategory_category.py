# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hype_venue', '0018_venuefacebookstat_fb_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venuecategory',
            name='category',
        ),
    ]
