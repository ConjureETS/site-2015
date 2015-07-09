from django.conf.urls import patterns, include, url
from member import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<member_id>\d+)$', views.show, name='show'),
)
