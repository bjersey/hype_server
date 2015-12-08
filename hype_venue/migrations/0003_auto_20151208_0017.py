# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hype_venue', '0002_auto_20151203_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='VenueRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=256)),
            ],
        ),
        migrations.AlterField(
            model_name='venue',
            name='hash_tags',
            field=django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=50, null=True, blank=True), blank=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='name',
            field=models.CharField(unique=True, max_length=256),
        ),
        migrations.AddField(
            model_name='venue',
            name='venue_region',
            field=models.ForeignKey(blank=True, to='hype_venue.VenueRegion', null=True),
        ),
    ]
