from django.conf.urls import patterns, include, url
from remenis.core import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from remenis import settings

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
#    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
#    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.login),
    url(r'^(\d+)/$', views.profile),
    url(r'^profile/$', views.profile),
    url(r'^home/$', views.feed),
    url(r'^notifications/$', views.notifications),
    url(r'^notifications/clear/$', views.notifications_clear),
    url(r'^whatsnext/$', views.whatsnext),
    url(r'^settings/$', views.settings_page),
    url(r'^post/$', views.post),
    url(r'^delete/$', views.delete),
    url(r'^comment/$', views.comment),
    url(r'^like/(\d+)/$', views.like),
    url(r'^searcherror/$', views.searcherror),
    url(r'^messagesent1/$', views.messagesent1),
    url(r'^messagesent2/$', views.messagesent2),
    url(r'^messagesent3/$', views.messagesent3),
    url(r'^story/(\d+)/$', views.story),
    url(r'^api/story/(\d+)/$', views.api_story),
    url(r'^mu-049a28c9-36388991-73c00a84-2c679173/$', views.blitz),
    url(r'^test_feed/(\d+)/(\w+)/$', views.test_feed),
    url(r'^test_story/(\d+)/(\d+)/(\w+)/$', views.test_story),
    
    url(r'^logout/$', views.logout),
)

urlpatterns += staticfiles_urlpatterns()

admin.autodiscover()

urlpatterns += patterns('',
    (r'^admin/', include(admin.site.urls)),
)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)