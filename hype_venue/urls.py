"""
Specifies all url patterns for this app.
"""
from django.conf.urls import url

from .views import VenueAPIView, VenueRegionAPIView, TickerAPIView

urlpatterns = [
    url(r'^venue/all/$', VenueAPIView.as_view()),
    url(r'^venueregion/all/$', VenueRegionAPIView.as_view()),
    url(r'^ticker/$', TickerAPIView.as_view()),
]
