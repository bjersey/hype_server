"""
Specifies all url patterns for this app.
"""
from django.conf.urls import url

from .views import LoginView

urlpatterns = [
    url(r'^login/$', LoginView.as_view()),
]
