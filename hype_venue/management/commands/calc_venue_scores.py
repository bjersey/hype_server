from django.core.management.base import BaseCommand
from hype_venue.models import Venue, VenueFacebookStat, VenueTwitterStat

from hype_venue.services import calc_venue_hype_score


class Command(BaseCommand):
    help = 'Rip through all venues and calculate hype score'

    def handle(self, *args, **options):

        all_venues = Venue.objects.all()

        all_venue_fb_stat = VenueFacebookStat.objects.all()
        all_venue_fb_stat_by_venue_id = {fb_stat.venue_id: fb_stat for fb_stat in all_venue_fb_stat}

        all_venue_twitter_stat = VenueTwitterStat.objects.all()
        all_venue_twitter_stat_by_venue_id = {twitter_stat.venue_id: twitter_stat for twitter_stat in all_venue_twitter_stat}

        for venue in all_venues:
            venue.score = calc_venue_hype_score(venue, all_venue_fb_stat_by_venue_id, all_venue_twitter_stat_by_venue_id)

            venue.save()

