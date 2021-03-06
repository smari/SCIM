from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, TemplateView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required

import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'mapper.views.home'),
	url(r'^maps/new/(?P<mapname>.+)/$', 'mapper.views.new'),
	url(r'^maps/(?P<id>\d+)/$', 'mapper.views.viewmap'),
	url(r'^maps/(?P<id>\d+)/resources/(?P<tier>\d+)/(?P<need>\d+)/$', 'mapper.views.get_resources' ),
	url(r'^maps/(?P<id>\d+)/resources/new/(?P<serviceproviders>(\d+[,]{0,1})+)/(?P<needs>(\d+[,]{0,1})+)/(?P<name>.+)/$', 'mapper.views.new_resouce'),
	url(r'^maps/(?P<id>\d+)/serviceprovider/(?P<tier>\d+)/$', 'mapper.views.get_serviceproviders' ),
	url(r'^maps/(?P<id>\d+)/serviceprovider/new/(?P<tier>\d+)/(?P<name>.+)/$', 'mapper.views.new_serviceprovider'),

	url(r'^about/$', TemplateView.as_view(template_name='about/how_scim_works.html')),
	url(r'^about/license/$', TemplateView.as_view(template_name='about/license.html')),
	url(r'^about/authors/$', TemplateView.as_view(template_name='about/authors.html')),
	url(r'^about/kittens/$', TemplateView.as_view(template_name='about/kittens.html')),

	(r'^accounts/', include('registration.urls')),
	url(r'^accounts/profile/$', 'mapper.views.home'),
	(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
