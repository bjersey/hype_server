import json

from django.core.management.base import BaseCommand
from hype_venue.models import Venue, VenueFacebookStat
from hype_core.constants import FB_GRAPH_VERSION, FB_APP_ID, FB_APP_SECRET


from hype_venue.constants import FB_FIELDS_TO_GET_FROM_VENUE

import facebook


class Command(BaseCommand):
    help = 'Rip through all venues and add categories from FB'

    def handle(self, *args, **options):
        try:
            graph = facebook.GraphAPI(access_token=FB_APP_ID + '|' + FB_APP_SECRET, version=FB_GRAPH_VERSION.strip('v'))

            all_venues = Venue.objects.all()

            for venue in all_venues:
                if venue.facebook_id:
                    try:
                        fb_object = graph.get_object(id=venue.facebook_id, fields=FB_FIELDS_TO_GET_FROM_VENUE)
                    except Exception as e:
                        print "inner exception"
                        # print "bad venue is" + str(venue.name)
                        print e.message
                        continue

                    venue_fb, just_created = VenueFacebookStat.objects.get_or_create(venue=venue, fb_id=fb_object['id'])

                    venue_fb.likes = fb_object.get('likes', None)
                    venue_fb.checkins = fb_object.get('checkins', None)
                    venue_fb.name = fb_object.get('name', None)
                    venue_fb.phone = fb_object.get('phone', None)
                    venue_fb.price_range = fb_object.get('price_range', None)
                    venue_fb.is_always_open = fb_object.get('is_always_open', None)
                    venue_fb.location = json.dumps(fb_object.get('location', None))
                    venue_fb.hours = json.dumps(fb_object.get('hours', None))

                    venue_fb.save()

        except Exception as e:
            print "outer exception"
            print e.message
