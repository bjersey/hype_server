from django.core.management.base import BaseCommand
from hype_venue.models import Venue, VenueInstagramStat

from datetime import timedelta
from django.utils import timezone

from hype_venue.constants import INSTAGRAM_REFRESH_INTERVAL_SECONDS

from instagram.client import InstagramAPI


class Command(BaseCommand):
    help = 'Rip through all venues and add IG followers'

    def handle(self, *args, **options):
        instagram_api = InstagramAPI(access_token='532975625.e47bd22.5a14ce36927442fab6c949d3695609a9',
                                     client_secret='4dd6e259faa849ab9fd39a8f354fe446')

        all_venues = Venue.objects.all()

        for venue in all_venues:
            # Get number of Instagram followers
            instagram_stat, _ = VenueInstagramStat.objects.get_or_create(venue=venue)

            # if timezone.now() > instagram_stat.updated_ts + timedelta(seconds=INSTAGRAM_REFRESH_INTERVAL_SECONDS) \
            #         and venue.instagram_id:
            if venue.instagram_id:
                try:
                    venue_insta_obj = instagram_api.user(venue.instagram_id)
                except Exception as e:
                    print e
                else:
                    if 'followed_by' in venue_insta_obj.counts:
                        instagram_stat.followers = venue_insta_obj.counts['followed_by']
                        instagram_stat.save()
