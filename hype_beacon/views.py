from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK

from hype_venue.models import Venue
from hype_user.models import UserFB
from hype_user.serializers import UserFBSerializer

from .models import UserVisit
from .serializers import UserVisitSerializer, BeaconSerializer


class UserVisitAPIView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request):
        all_user_visits = UserVisit.objects.all()

        all_users = [user_visit.user for user_visit in all_user_visits]

        all_beacons = [user_visit.beacon for user_visit in all_user_visits]

        all_users_fb = UserFB.objects.filter(user__in=all_users)

        data = {
            'user_visits': UserVisitSerializer(all_user_visits, many=True).data,
            'all_users_fb': UserFBSerializer(all_users_fb, many=True).data,
            'all_beacons': BeaconSerializer(all_beacons, many=True).data
        }

        return Response(data=data, status=HTTP_200_OK)

    def post(self, request):
        user = request.user
        venue_id = request.data['venue']

        venue_obj = Venue.objects.get(id=venue_id)

        user_visit, _ = UserVisit.objects.get_or_create(user=user, venue=venue_obj)

        return Response(data=UserVisitSerializer(user_visit).data, status=HTTP_200_OK)

    def delete(self, request):
        user = request.user
        venue_id = request.data['venue']

        venue_obj = Venue.objects.get(id=venue_id)

        UserVisit.objects.filter(user=user, venue=venue_obj).delete()
        return Response(status=200)

