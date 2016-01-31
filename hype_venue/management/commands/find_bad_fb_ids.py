from django.core.management.base import BaseCommand
from hype_venue.models import Venue
from hype_core.constants import FB_GRAPH_VERSION, FB_APP_ID, FB_APP_SECRET

import facebook


class Command(BaseCommand):
    help = 'Rip through all venues and find bad FB IDs'

    def handle(self, *args, **options):
        try:
            all_bad_names = []

            graph = facebook.GraphAPI(access_token=FB_APP_ID + '|' + FB_APP_SECRET, version=FB_GRAPH_VERSION.strip('v'))

            all_venues = Venue.objects.all()

            for venue in all_venues:
                if venue.facebook_id:
                    try:
                        graph.get_object(id=venue.facebook_id, fields='name')
                    except Exception as e:
                        print "start exception"
                        print "bad venue is " + venue.name
                        all_bad_names.append(venue.name)
                        print e.message
                        print "end exception"
                        continue

        except Exception as e:
            print "outer exception"
            print e.message
        else:
            print all_bad_names
