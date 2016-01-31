# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hype_venue', '0019_remove_venuecategory_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='venuecategory',
            name='category',
            field=django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128, null=True, blank=True), size=2), blank=True),
        ),
    ]
