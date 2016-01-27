from django.shortcuts import render
from rest_framework.views import APIView
import requests

# Create your views here.

FB_APP_SECRET = 'e45e8e3108085f10360a97b845174ac2'

class LoginView(APIView):
    def post(self, request):
        fb_access_token = request.data['fb_access_token']

        params = {'input_token': fb_access_token, 'access_token': FB_APP_SECRET}

        resp = requests.get('https://graph.facebook.com/debug_token', params=params)

        print resp
