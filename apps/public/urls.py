__author__ = 'macuser'

from django.conf.urls import patterns, url
from django.conf import settings
from views import *

urlpatterns = patterns(
    '',

    url(r'^events/$', EventList.as_view(), name='event-list'),
    url(r'^profile/$', UserProfile.as_view(), name='user-profile'),
)