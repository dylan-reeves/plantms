"""plantms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from equipment import views as equip

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^departments/(?P<department_id>[0-9]+)/$', equip.departmentdetail, name='departmentdetail'),
    url(r'^departments/create/', equip.departments_create, name='departments_create'),
    url(r'^departments/', equip.departments, name='departments'),
    url(r'^sites/', equip.sites, name='sites'),
    url(r'^equipment/', equip.equipment, name='equipment'),
    url(r'^$', equip.index, name='index'),
]
