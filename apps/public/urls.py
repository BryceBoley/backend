from django.conf.urls import patterns, url
from django.conf import settings
from views import *


urlpatterns = patterns(
    '',

    url(r'^events/$', EventList.as_view(), name='event_list'),
    url(r'^events/(?P<pk>[0-9]+)$', EventDetail.as_view(), name='event_detail'),
    url(r'^members/$', MemberList.as_view(), name='members_list'),
    url(r'^members/(?P<pk>[0-9]+)$', MemberDetail.as_view(), name='members_detail'),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)