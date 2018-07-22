from django.conf.urls import url
from django.contrib import admin
from shorten.views import create_shortcode, new_url, details_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<id>\d+)/$', new_url),
    url(r'^(?P<shortcode>[\w-]+)/$', details_view),
    url(r'^$', create_shortcode),
]
