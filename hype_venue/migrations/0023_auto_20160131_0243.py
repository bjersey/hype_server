# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hype_venue', '0022_venuecategory_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venuefacebookstat',
            name='category',
        ),
        migrations.AddField(
            model_name='venuefacebookstat',
            name='checkins',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='venuefacebookstat',
            name='is_always_open',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='venuefacebookstat',
            name='location',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='venuefacebookstat',
            name='name',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='venuefacebookstat',
            name='phone',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='venuefacebookstat',
            name='price_range',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
    ]
