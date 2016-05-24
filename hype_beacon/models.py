from django.db import models

from hype_core.models import TimeStampedModel


class Beacon(models.Model):

    uuid = models.CharField(max_length=1024)

    major = models.IntegerField()
    minor = models.IntegerField()

    venue = models.ForeignKey('hype_venue.Venue')

    def __unicode__(self):
        return self.uuid + '-' + str(self.major) + '-' + str(self.minor) + '-' + str(self.venue)


class UserVisit(TimeStampedModel):

    beacon = models.ForeignKey('hype_beacon.Beacon')

    user = models.ForeignKey('auth.User')

    def __unicode__(self):
        return str(self.beacon) + '_' + str(self.user)
