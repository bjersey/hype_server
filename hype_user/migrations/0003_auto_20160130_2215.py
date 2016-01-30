# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hype_user', '0002_userfb_fb_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfb',
            name='email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userfb',
            name='friends_count',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userfb',
            name='gender',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userfb',
            name='location_id',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userfb',
            name='name',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
    ]
