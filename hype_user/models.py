from django.db import models
from django.contrib.postgres.fields import ArrayField

from hype_core.models import TimeStampedModel
# Create your models here.


class UserFB(TimeStampedModel):
    user = models.ForeignKey('auth.User')
    fb_id = models.CharField(max_length=128)

    name = models.CharField(max_length=256, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    gender = models.CharField(max_length=32, null=True, blank=True)
    location_id = models.CharField(max_length=128, null=True, blank=True)
    friends_count = models.PositiveIntegerField(null=True, blank=True)

    likes = ArrayField(
        ArrayField(
            models.CharField(max_length=128, null=True, blank=True),
            size=2
        ),
        null=True, blank=True
    )

    def __unicode__(self):
        return self.name
