# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('score', models.IntegerField(null=True, blank=True)),
                ('address', models.CharField(max_length=1024)),
                ('website', models.CharField(max_length=512, null=True, blank=True)),
            ],
        ),
    ]
