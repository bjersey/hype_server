# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hype_venue', '0028_scoreparameters'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scoreparameters',
            name='data',
        ),
    ]
