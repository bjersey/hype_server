from rest_framework.serializers import ModelSerializer

from .models import UserVisit


class UserVisitSerializer(ModelSerializer):

    class Meta:
        model = UserVisit
        fields = ('user', 'beacon')
