# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hype_venue', '0030_scoreparameters_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='score',
            field=models.IntegerField(null=True, verbose_name=b'FIT Score', blank=True),
        ),
    ]
