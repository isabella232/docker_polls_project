from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include('docker_polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
