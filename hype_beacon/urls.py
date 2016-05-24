"""
Specifies all url patterns for this app.
"""
from django.conf.urls import url

from .views import UserVisitAPIView

urlpatterns = [
    url(r'^uservisit/$', UserVisitAPIView.as_view()),
]
