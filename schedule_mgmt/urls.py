"""schedule_mgmt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from schedule_mgmt.views import homepage, homepage_login, logout_view
from schedule.views import schedule_table
import statistics_module
from statistics_module import urls

urlpatterns = [
    url(r'admin/', include(admin.site.urls)),
    url(r'stats/', include(statistics_module.urls)),
    url(r'^homepage_login/$', homepage_login, name='homepage_login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^homepage/$', homepage, name="homepage"),
    url(r'^schedule_table/$', schedule_table, name="schedule_table"),
]
