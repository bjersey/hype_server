from django.db import models
from django.contrib.postgres.fields import ArrayField


class Venue(models.Model):
    name = models.CharField(max_length=256, unique=True)

    score = models.IntegerField(null=True, blank=True)

    address = models.CharField(max_length=1024)

    website = models.CharField(max_length=512, null=True, blank=True)

    facebook_id = models.CharField(max_length=32, null=True, blank=True)

    twitter_handle = models.CharField(max_length=32, null=True, blank=True)

    instagram_id = models.CharField(max_length=32, null=True, blank=True)

    hash_tags = ArrayField(models.CharField(max_length=50, null=True, blank=True), null=True, blank=True)

    venue_region = models.ForeignKey('hype_venue.VenueRegion', null=True, blank=True)

    def __unicode__(self):
        return self.name


class VenueRegion(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __unicode__(self):
        return self.name
