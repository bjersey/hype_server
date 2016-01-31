from django.contrib import admin

from .models import Venue, VenueRegion, VenueInstagramStat, VenueCategory, VenueFacebookStat, VenueTwitterStat


class VenueAdmin(admin.ModelAdmin):

    search_fields = ['hash_tags', 'name']

    list_display = ('name', 'score')

    class Meta:
        model = Venue

admin.site.register(Venue, VenueAdmin)
admin.site.register(VenueRegion)
admin.site.register(VenueInstagramStat)
admin.site.register(VenueCategory)
admin.site.register(VenueFacebookStat)
admin.site.register(VenueTwitterStat)
