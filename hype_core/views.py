from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.permissions import AllowAny

import requests

# Create your views here.
FB_APP_ID = '309453912512212'
FB_APP_SECRET = 'e45e8e3108085f10360a97b845174ac2'


class LoginView(APIView):

    permission_classes = (AllowAny, )

    def get(self, request):
        return Response(status=HTTP_200_OK)

    def post(self, request):
        fb_access_token = request.data['fb_access_token']

        params = {'input_token': fb_access_token, 'access_token': FB_APP_ID + '|' + FB_APP_SECRET}

        resp = requests.get('https://graph.facebook.com/debug_token', params=params)


        foo = resp.text

        bam = foo.replace("true", "True").replace("false", "False")

        user_data = eval(bam)

        fb_user_params = {'access_token': FB_APP_ID + '|' + FB_APP_SECRET,
                          'fields': 'name,gender,age_range,email,location,favorite_athletes,favorite_teams,first_name,last_name,friends,timezone'}

        user_info = requests.get("https://graph.facebook.com/v2.5/{0}".format(user_data['data']['user_id']), params=fb_user_params)

        print eval(user_info.text)

        return Response(data=resp, status=HTTP_200_OK)
