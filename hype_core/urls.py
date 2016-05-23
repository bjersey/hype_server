"""
Specifies all url patterns for this app.
"""
from django.conf.urls import url

from .views import FacebookLoginView

urlpatterns = [
    url(r'^login/fb/$', FacebookLoginView.as_view()),
]
