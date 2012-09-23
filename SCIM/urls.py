from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, TemplateView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required

import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'mapper.views.home'),
	url(r'^maps/new/', 'mapper.views.new'),
	url(r'^maps/(?P<id>\d+)/', 'mapper.views.viewmap'),
	url(r'^maps/resources/(?P<tier>\d+)/(?P<need>\d+)/', 'mapper.views.get_resources' ),
	url(r'^about/', TemplateView.as_view(template_name='about/how_scim_works.html')),

	(r'^accounts/', include('registration.urls')),
	url(r'^accounts/profile/$', UpdateView.as_view(success_url="/accounts/profile/")),
	(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
