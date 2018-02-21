from django.conf.urls import url
from statistics_module.views import statistics_home, statistics_result, statistics_search

urlpatterns = [
    url(r'^statistics_home/$', statistics_home, name='statistics_home'),
    url(r'^statistics_result/$', statistics_result, name='statistics_result'),
    url(r'^statistics_search/$', statistics_search, name='statistics_search'),
]