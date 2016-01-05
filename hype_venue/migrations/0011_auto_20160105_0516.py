# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hype_venue', '0010_venueinstagramstat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venueinstagramstat',
            name='followers',
            field=models.IntegerField(default=0),
        ),
    ]
