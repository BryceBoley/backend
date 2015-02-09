from django.conf.urls import patterns, url
from django.conf import settings
from views import *


urlpatterns = patterns(
    '',

    url(r'^events/$', EventList.as_view(), name='event_list'),
    url(r'^add_event$', AddEvent.as_view(), name='add_event'),
    url(r'^members/$', MemberList.as_view(), name='members_list'),
    url(r'^add_member$', AddMember.as_view(), name='add_member'),
    url(r'^events/(?P<pk>[0-9]+)$', DeleteEvent.as_view(), name='delete_event'),
    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    # url(r'^profile', UserProfile.as_view(), name='user_profile'),

)