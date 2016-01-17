from django.db import models
from django.contrib.postgres.fields import ArrayField

from hype_core.models import TimeStampedModel


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

    capacity = models.IntegerField(null=True, blank=True)

    category = models.ManyToManyField('hype_venue.VenueCategory')

    def __unicode__(self):
        return self.name


class VenueCategory(models.Model):

    category = models.CharField(max_length=256, unique=True)

    def __unicode__(self):
        return self.category


class VenueRegion(models.Model):
    name = models.CharField(max_length=256, unique=True)

    city = models.ForeignKey('cities_light.City')

    def __unicode__(self):
        return self.name


class VenueInstagramStat(TimeStampedModel):
    venue = models.ForeignKey('hype_venue.Venue')
    followers = models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.venue)
