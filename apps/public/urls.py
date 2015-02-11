from django.conf.urls import patterns, url
from django.conf import settings
from views import *


urlpatterns = patterns(
    '',

    url(r'^events/$', EventList.as_view(), name='event_list'),
    url(r'^add_event$', AddEvent.as_view(), name='add_event'),
    url(r'^members/$', MemberList.as_view(), name='members_list'),
    url(r'^add_member$', AddMember.as_view(), name='add_member'),
    url(r'^edit_event/(?P<pk>[0-9]+)$', EditEvent.as_view(), name='event_list'),
    url(r'^edit_member/(?P<pk>[0-9]+)$', EditMember.as_view(), name='members_list'),
    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

)