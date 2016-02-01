from django.contrib import admin
from django.core.management import call_command

from .models import Venue, VenueRegion, VenueInstagramStat, VenueCategory, VenueFacebookStat, VenueTwitterStat, ScoreParameters


class VenueAdmin(admin.ModelAdmin):

    search_fields = ['hash_tags', 'name']

    list_display = ('name', 'facebook_likes', 'facebook_checkins', 'twitter_followers', 'score', 'venue_region')

    list_filter = ('venue_region', )

    actions = ['update_facebook_stat', 'update_twitter_stat']

    def update_facebook_stat(self, request, queryset):
        call_command('add_fb_venue_data', venues=queryset)
        call_command('calc_venue_scores')
    update_facebook_stat.short_description = "Update Facebook statistics"

    def update_twitter_stat(self, request, queryset):
        call_command('add_twitter_data', venues=queryset)
        call_command('calc_venue_scores')
    update_twitter_stat.short_description = "Update Twitter statistics"

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
