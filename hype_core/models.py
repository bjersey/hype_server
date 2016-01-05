from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):
    updated_ts = models.DateTimeField(auto_now=True)
    created_ts = models.DateTimeField(auto_now_add=True)
