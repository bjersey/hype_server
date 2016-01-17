from django.core.management.base import BaseCommand
from hype_venue.models import Venue, VenueCategory

import facebook

fb_access_token = 'CAAEZAclqHltQBALyEW4S7GKl7Vf9vRKC57nOBJwKSUejTjRNGL9B8M6dhlZBIzkj9XTZA5nReqNJPkCz5oukZAQhLXwJ1eFVaZBmZBkPca53Y1H5S1qkbvvz2ZAmCV8krHwcPPgQFFfsXRDi5BUrog4Jum1KlHrhwQOtv85h9GnIK7VjJG97auNIq0nVoOM1xLDLR4G79NI28VNN4U13UZBN'


class Command(BaseCommand):
    help = 'Rip through all venues and add categories from FB'

    def handle(self, *args, **options):
        try:
            graph = facebook.GraphAPI(access_token=fb_access_token, version='2.5')

            all_venues = Venue.objects.all()

            for venue in all_venues:
                fb_object = graph.get_object(id=venue.facebook_id, fields='category_list')

                for cat in fb_object['category_list']:
                    obj, _ = VenueCategory.objects.get_or_create(name=cat['name'])

                    venue.category.add(obj)
                    venue.save()
        except Exception as e:
            print(e)