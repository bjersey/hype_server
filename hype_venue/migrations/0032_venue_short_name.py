# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hype_venue', '0031_auto_20160131_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='short_name',
            field=models.CharField(max_length=16, null=True, blank=True),
        ),
    ]
