"""
Specifies all url patterns for this app.
"""
from django.conf.urls import url

from .views import VenueAPIView

urlpatterns = [
    url(r'^all/$', VenueAPIView.as_view()),
]