from rest_framework import serializers

from .models import Venue


class VenueSerializer(serializers.ModelSerializer):
    score = serializers.IntegerField()

    class Meta:
        model = Venue
        fields = ('id', 'name', 'address', 'website', 'score')