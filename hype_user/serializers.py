from django.contrib.auth.models import User

from rest_framework.serializers import ModelSerializer

from .models import UserFB


class UserFBSerializer(ModelSerializer):

    class Meta:
        model = UserFB
        fields = ('id', 'fb_id', 'name', 'user')


# class UserSerializer(ModelSerializer):
#
#     class Meta:
#         model = User
#         fields = ('id')