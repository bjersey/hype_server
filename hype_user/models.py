from django.db import models
from hype_core.models import TimeStampedModel
# Create your models here.


class UserFB(TimeStampedModel):
    user = models.ForeignKey('auth.User')
