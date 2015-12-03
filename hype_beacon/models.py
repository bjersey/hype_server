from django.db import models


class Beacon(models.Model):

    uuid = models.CharField(max_length=1024)

    major = models.IntegerField()
    minor = models.IntegerField()

    venue = models.ForeignKey('hype_venue.Venue')

    def __unicode__(self):
        return self.uuid + '-' + str(self.major) + '-' + str(self.minor) + '-' + str(self.venue)

