__author__ = 'mrk2'
from django.conf.urls import url, patterns
from api import views



urlpatterns = patterns(
    'api.views',
    #url(r'^country/$',views.CountrySerializer,name='country'),
    url(r'^get_country/$','get_country', name='get_country'),
    url(r'^get_state/(?P<sid>[\w-]+)/$', 'get_state', name='get_state'),
    url(r'^get_city/(?P<cid>[\w-]+)/$', 'get_city', name='get_city'),
    )