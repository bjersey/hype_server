from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED
from rest_framework.permissions import AllowAny

import requests

from .constants import FB_GRAPH_VERSION, FB_APP_ID, FB_APP_SECRET

FB_FIELDS_TO_GET_FROM_USER = 'name,gender,age_range,email,location,favorite_athletes,favorite_teams,first_name,last_name,friends,timezone'


class LoginView(APIView):

    permission_classes = (AllowAny, )

    def get(self, request):
        return Response(status=HTTP_200_OK)

    def post(self, request):
        fb_access_token = request.data['fb_access_token']

        params = {'input_token': fb_access_token, 'access_token': FB_APP_ID + '|' + FB_APP_SECRET}

        resp = requests.get('https://graph.facebook.com/{0}/debug_token'.format(FB_GRAPH_VERSION), params=params)

        response_text = resp.text.replace("true", "True").replace("false", "False")

        user_token_data = eval(response_text)

        if user_token_data['data']['is_valid'] == True and user_token_data['data']['app_id'] == FB_APP_ID \
                and user_token_data['data']['application'] == 'hype':

            fb_user_params = {'access_token': FB_APP_ID + '|' + FB_APP_SECRET, 'fields': FB_FIELDS_TO_GET_FROM_USER}

            user_info = requests.get("https://graph.facebook.com/{0}/{1}".format(
                    FB_GRAPH_VERSION, user_token_data['data']['user_id']), params=fb_user_params)

            print eval(user_info.text)
            
            status = HTTP_200_OK
        else:
            status = HTTP_401_UNAUTHORIZED

        return Response(status=status)
