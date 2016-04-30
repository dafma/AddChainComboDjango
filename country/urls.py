__author__ = 'mrk2'
from django.conf.urls import url, patterns
from api import views
from .views import render_country

urlpatterns = patterns(
    '',
    url(r'render/$', render_country, name="render_country"),
    #url(r'user_country/$', 'country.views.getUserCountry', name="get_user_country"),

    )