from .models import Venue, VenueInstagramStat
from .serializers import VenueSerializer
from .constants import INSTAGRAM_REFRESH_INTERVAL_SECONDS

from random import randint

from datetime import datetime, timedelta

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response

from instagram.client import InstagramAPI
from instagram.bind import InstagramAPIError



class VenueAPIView(APIView):

    permission_classes = (AllowAny, )

    def get(self, request):
        instagram_api = InstagramAPI(access_token='532975625.e47bd22.5a14ce36927442fab6c949d3695609a9',
                                     client_secret='4dd6e259faa849ab9fd39a8f354fe446')

        all_venues = Venue.objects.all()

        for venue in all_venues:
            # Get number of Instagram followers
            instagram_stat, created = VenueInstagramStat.objects.get_or_create(venue=venue)

            if datetime.utcnow() > instagram_stat.updated_ts + timedelta(seconds=INSTAGRAM_REFRESH_INTERVAL_SECONDS):
                try:
                    venue_insta_obj = instagram_api.user(venue.instagram_id)
                except Exception as e:
                    print e
                else:
                    instagram_stat.followers = venue_insta_obj.counts['followed_by']

        return Response(data=VenueSerializer(all_venues, many=True).data, status=HTTP_200_OK)
