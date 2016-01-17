from django.contrib import admin

from .models import Venue, VenueRegion, VenueInstagramStat


class VenueAdmin(admin.ModelAdmin):

    search_fields = 'hash_tags'

    class Meta:
        model = Venue

admin.site.register(Venue, VenueAdmin)
admin.site.register(VenueRegion)
admin.site.register(VenueInstagramStat)
