from django.contrib import admin
from django.core.management import call_command

from .models import Venue, VenueRegion, VenueInstagramStat, VenueCategory, VenueFacebookStat, VenueTwitterStat, ScoreParameters


class VenueAdmin(admin.ModelAdmin):

    search_fields = ['hash_tags', 'name']

    list_display = ('name', 'score')

    class Meta:
        model = Venue


class ScoreParametersAdmin(admin.ModelAdmin):

    def update_scores(self, request, queryset):
        call_command('calc_venue_scores')

    actions = ['update_scores']

    class Meta:
        model = ScoreParameters


admin.site.register(Venue, VenueAdmin)
admin.site.register(ScoreParameters, ScoreParametersAdmin)
admin.site.register(VenueRegion)
admin.site.register(VenueInstagramStat)
admin.site.register(VenueCategory)
admin.site.register(VenueFacebookStat)
admin.site.register(VenueTwitterStat)
