from rest_framework.serializers import ModelSerializer

from .models import UserVisit, Beacon


class UserVisitSerializer(ModelSerializer):

    class Meta:
        model = UserVisit
        fields = ('user', 'beacon')


class BeaconSerializer(ModelSerializer):

    class Meta:
        model = Beacon
        fields = ('id', 'uuid', 'major', 'minor', 'venue')
