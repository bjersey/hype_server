from django.core.management.base import BaseCommand
from hype_venue.models import Venue, VenueCategory
from hype_core.constants import FB_GRAPH_VERSION, FB_APP_ID, FB_APP_SECRET

import facebook


class Command(BaseCommand):
    help = 'Rip through all venues and add categories from FB'

    def handle(self, *args, **options):
        try:
            graph = facebook.GraphAPI(access_token=FB_APP_ID + '|' + FB_APP_SECRET, version=FB_GRAPH_VERSION.strip('v'))

            if 'venues' not in options:
                all_venues = Venue.objects.all()
            else:
                all_venues = options['venues']

            for venue in all_venues:
                if venue.facebook_id:
                    try:
                        fb_object = graph.get_object(id=venue.facebook_id, fields='category_list')
                    except Exception as e:
                        print "start exception"
                        # print "bad venue is " + str(venue.name)
                        print e.message
                        print "end exception"
                        continue

                    if 'category_list' in fb_object:
                        for cat in fb_object['category_list']:
                            category = VenueCategory.objects.filter(category__contains=[cat['id'], cat['name']])

                            if not category:
                                category = [VenueCategory.objects.create(category=[cat['id'], cat['name']])]

                            venue.category.add(category[0])

                        venue.save()


        except Exception as e:
            print "outer exception"
            print venue.name
            print e.message
