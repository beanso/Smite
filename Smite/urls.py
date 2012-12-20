from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from Smitedb.models import Player
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Smitedb.views.top_rated'),
    url(r'^player/', 'Smitedb.views.player')
    # url(r'^Smite/', include('Smite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
