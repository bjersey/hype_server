from django.db import models


class Beacon(models.Model):

    uuid = models.CharField(max_length=1024)

    major = models.IntegerField()
    minor = models.IntegerField()

    venue = models.ForeignKey('hype_venue.Venue')

