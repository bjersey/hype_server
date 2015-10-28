from .models import Venue
from .serializers import VenueSerializer

from random import randint

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response



class VenueAPIView(APIView):

    permission_classes = (AllowAny, )

    def get(self, request):
        all_venues = Venue.objects.all()

        for venue in all_venues:
            venue.score = randint(0, 100)

        return Response(data=VenueSerializer(all_venues, many=True).data, status=HTTP_200_OK)
