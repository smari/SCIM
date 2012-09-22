from django.conf.urls.defaults import patterns, include, url
rom django.views.generic import ListView, TemplateView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required

import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'mapper.views.home'),

	(r'^accounts/', include('registration.urls')),
	(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
