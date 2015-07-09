from django.conf.urls import patterns, include, url
from django.contrib import admin
from conjure import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'conjure.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^membres/', include('member.urls', namespace='member')),
    url(r'^projets/', include('project.urls', namespace='project')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^ckeditor/', include('ckeditor.urls')),
)
