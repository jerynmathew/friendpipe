from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'friendpipe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'core.chat.views.chat_home', name='home'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
