from django.contrib import admin

from .models import Beacon, UserVisit

admin.site.register(Beacon)
admin.site.register(UserVisit)
