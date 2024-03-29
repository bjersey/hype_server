from hype_venue.services import calc_venue_hype_score, get_venue_regions, get_venues
from .models import Venue, VenueInstagramStat, VenueRegion, VenueTwitterStat, VenueFacebookStat, TickerText
from .serializers import VenueSerializer, VenueRegionSerializer, TickerTextSerializer
from .constants import INSTAGRAM_REFRESH_INTERVAL_SECONDS

from random import randint

from datetime import datetime, timedelta
from django.utils import timezone

from django.db.models import Count

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response

from instagram.client import InstagramAPI
from instagram.bind import InstagramAPIError


class TickerAPIView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request):
        ticker_qs = TickerText.objects.all()

        if ticker_qs:
            ticker = ticker_qs[0]
        else:
            ticker = None

        return Response(data=TickerTextSerializer(ticker).data, status=HTTP_200_OK)


class VenueRegionAPIView(APIView):

    permission_classes = (AllowAny, )

    def get(self, request):

        all_venue_regions = get_venue_regions()

        return Response(data=VenueRegionSerializer(all_venue_regions, many=True).data, status=HTTP_200_OK)


class VenueAPIView(APIView):

    permission_classes = (AllowAny, )

    def get(self, request):
        # instagram_api = InstagramAPI(access_token='532975625.e47bd22.5a14ce36927442fab6c949d3695609a9',
        #                              client_secret='4dd6e259faa849ab9fd39a8f354fe446')

        all_venues = get_venues()

        all_venue_fb_stat = VenueFacebookStat.objects.filter(venue__in=all_venues)
        all_venue_fb_stat_by_venue_id = {fb_stat.venue_id: fb_stat for fb_stat in all_venue_fb_stat}

        all_venue_twitter_stat = VenueTwitterStat.objects.filter(venue__in=all_venues)
        all_venue_twitter_stat_by_venue_id = {twitter_stat.venue_id: twitter_stat for twitter_stat in all_venue_twitter_stat}

        for venue in all_venues:
            fb_stat = all_venue_fb_stat_by_venue_id.get(venue.id)
            twitter_stat = all_venue_twitter_stat_by_venue_id.get(venue.id)

            venue.fb_likes = getattr(fb_stat, 'likes', None)
            venue.checkins = getattr(fb_stat, 'checkins', None)
            venue.followers_count = getattr(twitter_stat, 'followers_count', None)

        # for venue in all_venues:
        #     # Get number of Instagram followers
        #     instagram_stat, created = VenueInstagramStat.objects.get_or_create(venue=venue)
        #
        #     if timezone.now() > instagram_stat.updated_ts + timedelta(seconds=INSTAGRAM_REFRESH_INTERVAL_SECONDS) \
        #             and venue.instagram_id:
        #         try:
        #             venue_insta_obj = instagram_api.user(venue.instagram_id)
        #         except Exception as e:
        #             print e
        #         else:
        #             instagram_stat.followers = venue_insta_obj.counts['followed_by']
        #             instagram_stat.save()

        return Response(data=VenueSerializer(all_venues, many=True).data, status=HTTP_200_OK)
