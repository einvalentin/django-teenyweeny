from django.conf.urls import patterns, include, url
from .views import ExpandRedirectView

urlpatterns = patterns('',
    url(r'^(?P<short_link>[-\w]+)$', ExpandRedirectView.as_view(), name='redirect'),
)
