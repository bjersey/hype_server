# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def set_clarendon_region(apps, schema_editor):
    Venue = apps.get_model("hype_venue", "Venue")
    VenueRegion = apps.get_model("hype_venue", "VenueRegion")
    venue_region = VenueRegion.objects.first()
    for venue in Venue.objects.all():
        venue.venue_region = venue_region
        venue.save()

class Migration(migrations.Migration):

    dependencies = [
        ('hype_venue', '0006_auto_20151208_0532'),
    ]

    operations = [
        migrations.RunPython(set_clarendon_region),
    ]
