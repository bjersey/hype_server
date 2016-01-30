# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hype_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfb',
            name='fb_id',
            field=models.CharField(default='foobar', max_length=128),
            preserve_default=False,
        ),
    ]
