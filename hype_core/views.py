from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED
from rest_framework.permissions import AllowAny
from django.contrib.auth import login, authenticate


FB_FIELDS_TO_GET_FROM_USER = 'name,gender,age_range,email,location,favorite_athletes,favorite_teams,first_name,last_name,friends,timezone,likes'


class FacebookLoginView(APIView):

    permission_classes = (AllowAny, )

    def get(self, request):

        if request.user.is_authenticated():
            return Response(status=200)
        else:
            return Response(status=401)

    def post(self, request):
        fb_access_token = request.data['fb_access_token']

        if request.user.is_authenticated():
            return Response(status=200)

        user = authenticate(token=fb_access_token)

        if user:
            login(request, user)

            status = HTTP_200_OK
        else:
            status = HTTP_401_UNAUTHORIZED

        return Response(status=status)
