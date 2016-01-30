# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hype_user', '0003_auto_20160130_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfb',
            name='likes',
            field=django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128, null=True, blank=True), size=2), blank=True),
        ),
    ]
