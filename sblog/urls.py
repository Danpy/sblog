from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from blog.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sblog.views.home', name='home'),
    # url(r'^sblog/', include('sblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^$', blogs),
    url(r'^about/', about),
    url(r'^blogs', tag_to_blogs),
    url(r'^blog/(?P<id>\d{1,50})', blog),
    url(r'^readings', readings),
)
