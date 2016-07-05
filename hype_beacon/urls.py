"""
Specifies all url patterns for this app.
"""
from django.conf.urls import url

from .views import UserVisitAPIView, BeaconAPIView

urlpatterns = [
    url(r'^uservisit/$', UserVisitAPIView.as_view()),
    url(r'^beacons/$', BeaconAPIView.as_view()),
]
