from .models import Venue
from .serializers import VenueSerializer

from random import randint

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response

from instagram.client import InstagramAPI
from instagram.bind import InstagramAPIError



class VenueAPIView(APIView):

    permission_classes = (AllowAny, )

    instagram_api = InstagramAPI(access_token='532975625.e47bd22.5a14ce36927442fab6c949d3695609a9',
                                 client_secret='4dd6e259faa849ab9fd39a8f354fe446')

    def get(self, request):
        all_venues = Venue.objects.all()

        for venue in all_venues:
            # Get number of Instagram followers
            try:
                venue_insta_obj = self.instagram_api.user(venue.instagram_id)
            except InstagramAPIError as e:
                print e
                venue.instagram_followers = None
            else:
                venue.instagram_followers = venue_insta_obj.counts['followed_by']



        return Response(data=VenueSerializer(all_venues, many=True).data, status=HTTP_200_OK)
