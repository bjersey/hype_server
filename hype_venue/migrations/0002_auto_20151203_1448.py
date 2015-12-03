# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hype_venue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='facebook_id',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='hash_tags',
            field=django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=10, null=True, blank=True), blank=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='instagram_id',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='twitter_handle',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
    ]
