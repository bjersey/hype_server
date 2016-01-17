# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hype_venue', '0011_auto_20160105_0516'),
    ]

    operations = [
        migrations.CreateModel(
            name='VenueCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(unique=True, max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='venue',
            name='category',
            field=models.ManyToManyField(to='hype_venue.VenueCategory'),
        ),
    ]
