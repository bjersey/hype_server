# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.contrib.postgres.operations import HStoreExtension


class Migration(migrations.Migration):

    dependencies = [
        ('hype_venue', '0026_venuefacebookstat_hours'),
    ]

    operations = [
        HStoreExtension()
    ]
