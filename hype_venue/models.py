from django.db import models
from django.contrib.postgres.fields import ArrayField
from django_hstore import hstore

from hype_core.models import TimeStampedModel


class Venue(models.Model):
    name = models.CharField(max_length=256, unique=True)

    short_name = models.CharField(max_length=16, null=True, blank=True)

    score = models.IntegerField(null=True, blank=True, verbose_name='FIT Score')

    address = models.CharField(max_length=1024)

    website = models.CharField(max_length=512, null=True, blank=True)

    facebook_id = models.CharField(max_length=32, null=True, blank=True)

    twitter_handle = models.CharField(max_length=32, null=True, blank=True)

    instagram_id = models.CharField(max_length=32, null=True, blank=True)
    instagram_location_id = models.CharField(max_length=32, null=True, blank=True)

    hash_tags = ArrayField(models.CharField(max_length=50, null=True, blank=True), null=True, blank=True)

    venue_region = models.ForeignKey('hype_venue.VenueRegion', null=True, blank=True)

    capacity = models.IntegerField(null=True, blank=True)

    category = models.ManyToManyField('hype_venue.VenueCategory', blank=True)

    def __unicode__(self):
        return self.name


class VenueCategory(models.Model):

    category = ArrayField(models.CharField(max_length=128, null=True, blank=True), size=2, null=True, blank=True)

    def __unicode__(self):
        return str(self.category)


class VenueRegion(models.Model):
    name = models.CharField(max_length=256, unique=True)

    city = models.ForeignKey('cities_light.City')

    def __unicode__(self):
        return self.name


class VenueInstagramStat(TimeStampedModel):
    venue = models.ForeignKey('hype_venue.Venue')
    followers = models.IntegerField(null=True, blank=True)
    tag_count = models.PositiveIntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.venue.name


class VenueFacebookStat(TimeStampedModel):
    venue = models.ForeignKey('hype_venue.Venue')

    fb_id = models.CharField(max_length=128)

    likes = models.IntegerField(null=True, blank=True)
    checkins = models.PositiveIntegerField(null=True, blank=True)
    name = models.CharField(max_length=128, null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    price_range = models.CharField(max_length=32, null=True, blank=True)
    location = models.CharField(max_length=512, null=True, blank=True)
    hours = models.CharField(max_length=512, null=True, blank=True)
    is_always_open = models.NullBooleanField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class VenueTwitterStat(TimeStampedModel):
    venue = models.ForeignKey('hype_venue.Venue')

    twitter_id = models.CharField(max_length=128)
    name = models.CharField(max_length=128, null=True, blank=True)
    followers_count = models.PositiveIntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class ScoreParameters(TimeStampedModel):
    name = models.CharField(max_length=32)

    data = hstore.DictionaryField(null=True, blank=True)

    objects = hstore.HStoreManager()

    def __unicode__(self):
        return self.name


class TickerText(TimeStampedModel):
    text = models.CharField(max_length=32, null=True, blank=True)

    def __unicode__(self):
        return self.text
