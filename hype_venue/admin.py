from django.contrib import admin
from django.core.management import call_command

from .models import Venue, VenueRegion, VenueInstagramStat, VenueCategory, VenueFacebookStat, VenueTwitterStat, ScoreParameters


class VenueAdmin(admin.ModelAdmin):

    search_fields = ['hash_tags', 'name']

    list_display = ('name', 'facebook_likes', 'facebook_checkins', 'twitter_followers', 'score')

    def facebook_likes(self, obj):
        fb_stat = VenueFacebookStat.objects.filter(venue=obj)
        if fb_stat:
            return fb_stat[0].likes
        else:
            return None
    facebook_likes.short_description = 'Facebook Likes'

    def facebook_checkins(self, obj):
        fb_stat = VenueFacebookStat.objects.filter(venue=obj)
        if fb_stat:
            return fb_stat[0].checkins
        else:
            return None
    facebook_checkins.short_description = 'Facebook Checkins'

    def twitter_followers(self, obj):
        twitter_stat = VenueTwitterStat.objects.filter(venue=obj)
        if twitter_stat:
            return twitter_stat[0].followers_count
        else:
            return None
    twitter_followers.short_description = 'Twitter Followers'

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
