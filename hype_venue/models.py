from django.db import models


class Venue(models.Model):
    name = models.CharField(max_length=256)

    score = models.IntegerField(null=True, blank=True)

    address = models.CharField(max_length=1024)

    website = models.CharField(max_length=512, null=True, blank=True)
