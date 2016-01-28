from django.core.management.base import BaseCommand
from hype_venue.models import Venue, VenueCategory

import facebook

fb_access_token = 'CAAEZAclqHltQBAMoZBbg5eZCxaJ4uW6pFtfwsGnmno052JwRuUnKk07AgqpaY7q7nTaPnO7FSGZCE2hCjZBfTvl4oazNZAF9RVprMAb1ZBj3igE21ntaJIUStCuxj8HSuVEdpLdPZC3rouBTv6OPaWcnlvEYPkPRwqwUC5kZBunHMcTD0lkQNdbbBJR99ZBjOJVXWpqA8vpREcMWUn1Dut2x7d'


class Command(BaseCommand):
    help = 'Rip through all venues and add categories from FB'

    def handle(self, *args, **options):
        try:
            graph = facebook.GraphAPI(access_token=fb_access_token, version='2.5')

            all_venues = Venue.objects.all()

            for venue in all_venues:
                if venue.facebook_id:
                    try:
                        fb_object = graph.get_object(id=venue.facebook_id, fields='category_list')
                    except Exception as e:
                        print "inner exception"
                        print "bad venue is" + str(venue.name)
                        print e.message
                        continue

                    for cat in fb_object['category_list']:
                        obj, _ = VenueCategory.objects.get_or_create(category=cat['name'])

                        venue.category.add(obj)
                        venue.save()
        except Exception as e:
            print "outer exception"
            print e.message
