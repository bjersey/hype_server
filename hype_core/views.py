from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
import requests

from .constants import FB_GRAPH_VERSION, FB_APP_ID, FB_APP_SECRET

from hype_user.models import UserFB

FB_FIELDS_TO_GET_FROM_USER = 'name,gender,age_range,email,location,favorite_athletes,favorite_teams,first_name,last_name,friends,timezone,likes'


class LoginView(APIView):

    permission_classes = (AllowAny, )

    def get(self, request):
        return Response(status=HTTP_200_OK)

    def post(self, request):
        fb_access_token = request.data['fb_access_token']

        params = {'input_token': fb_access_token, 'access_token': FB_APP_ID + '|' + FB_APP_SECRET}

        resp = requests.get('https://graph.facebook.com/{0}/debug_token'.format(FB_GRAPH_VERSION), params=params)

        response_text = resp.text.replace("true", "True").replace("false", "False")

        user_token_data = eval(response_text)['data']

        if user_token_data['is_valid'] == True and user_token_data['app_id'] == FB_APP_ID \
                and user_token_data['application'] == 'hype':

            fb_user_params = {'access_token': FB_APP_ID + '|' + FB_APP_SECRET, 'fields': FB_FIELDS_TO_GET_FROM_USER}

            user_info = requests.get("https://graph.facebook.com/{0}/{1}".format(
                    FB_GRAPH_VERSION, user_token_data['user_id']), params=fb_user_params)

            user_info_dict = eval(user_info.text)

            user_model = get_user_model()

            user, just_created = user_model.objects.get_or_create(email=user_info_dict['email'])

            if just_created:
                user.username = user_info_dict['email']
                user.first_name = user_info_dict['first_name']
                user.last_name = user_info_dict['last_name']
                user.set_unusable_password()
                user.save()

            user_fb, _ = UserFB.objects.get_or_create(user=user, fb_id=user_info_dict['id'])

            user_fb.name = user_info_dict.get('name')
            user_fb.email = user_info_dict.get('email')
            user_fb.gender = user_info_dict.get('gender')
            location_info = user_info_dict.get('location')
            if location_info:
                user_fb.location_id = location_info['id']
            if 'friends' in user_info_dict:
                user_fb.friends_count = user_info_dict['friends']['summary']['total_count']

            # reset likes:
            user_fb.likes = []
            for like in user_info_dict['likes']['data']:
                user_fb.likes.append([like['id'], like['name']])

            user_fb.save()

            status = HTTP_200_OK
        else:
            status = HTTP_401_UNAUTHORIZED

        return Response(status=status)
