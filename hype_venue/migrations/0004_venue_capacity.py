# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hype_venue', '0003_auto_20151208_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='capacity',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
