from django.core.management.base import BaseCommand

import twitter

from hype_core.constants import (TWITTER_APP_KEY, TWITTER_APP_SECRET, TWITTER_TOKEN, TWITTER_TOKEN_SECRET)
from hype_venue.models import Venue, VenueTwitterStat


class Command(BaseCommand):
    help = 'Rip through all venues and add twitter follower data'

    def handle(self, *args, **options):
        try:

            api = twitter.Api(consumer_key=TWITTER_APP_KEY, consumer_secret=TWITTER_APP_SECRET,
                              access_token_key=TWITTER_TOKEN, access_token_secret=TWITTER_TOKEN_SECRET)

            all_venues = Venue.objects.all()

            for venue in all_venues:
                if venue.twitter_handle:
                    try:
                        if VenueTwitterStat.objects.filter(venue=venue):
                            twitter_object = api.GetUser(screen_name=venue.twitter_handle)
                    except twitter.error.TwitterError as e:
                        print "inner exception"
                        # print "bad venue is" + str(venue.name)
                        print e.message
                        continue

                    venue_twitter, just_created = VenueTwitterStat.objects.get_or_create(venue=venue,
                                                                                         twitter_id=str(twitter_object.id))

                    venue_twitter.name = getattr(twitter_object, 'name', None)
                    venue_twitter.followers_count = getattr(twitter_object, 'followers_count', None)

                    venue_twitter.save()

        except Exception as e:
            print "outer exception"
            print e.message