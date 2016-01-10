from rest_framework import serializers

from .models import Venue, VenueRegion


class VenueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Venue
        fields = ('id', 'name', 'address', 'website', 'score', 'facebook_id', 'instagram_id', 'twitter_handle',
                  'hash_tags', 'venue_region')


class VenueRegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = VenueRegion
        fields = ('id', 'name', 'city')
