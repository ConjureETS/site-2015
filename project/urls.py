from django.conf.urls import patterns, include, url
from project import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<project_id>\d+)$', views.show, name='show'),
)
