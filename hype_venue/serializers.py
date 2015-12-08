from rest_framework import serializers

from .models import Venue


class VenueSerializer(serializers.ModelSerializer):
    instagram_followers = serializers.IntegerField()

    class Meta:
        model = Venue
        fields = ('id', 'name', 'address', 'website', 'score', 'facebook_id', 'instagram_id', 'twitter_handle',
                  'hash_tags', 'instagram_followers')