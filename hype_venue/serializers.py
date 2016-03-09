from rest_framework import serializers

from .models import Venue, VenueRegion, TickerText


class VenueSerializer(serializers.ModelSerializer):

    followers_count = serializers.IntegerField(read_only=True)
    checkins = serializers.IntegerField(read_only=True)
    fb_likes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Venue
        fields = ('id', 'name', 'address', 'website', 'score', 'facebook_id', 'instagram_id', 'twitter_handle',
                  'hash_tags', 'venue_region', 'followers_count', 'checkins', 'fb_likes', 'short_name')


class VenueRegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = VenueRegion
        fields = ('id', 'name', 'city')


class TickerTextSerializer(serializers.ModelSerializer):

    class Meta:
        model = TickerText
        fields = ('text', )
