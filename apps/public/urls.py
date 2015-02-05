from django.conf.urls import patterns, url
from django.conf import settings
from views import *


urlpatterns = patterns(
	'',

	url(r'^events/$', DinnerList.as_view(), name='events'),
	url(r'^add-event/$', NewDinner.as_view(), name='add-event'),
	url(r'^event/(?P<pk>[0-9]+)$', EditDinner.as_view(), name='event'),
	# url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
