from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vsafe.views.home', name='home'),
    # url(r'^vsafe/', include('vsafe.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'website.views.index'),
    url(r'^learn/', 'website.views.learn'),
    url(r'^browse/$', 'website.views.browse'),
    url(r'^browse/ingredient/[0-9]+$', 'website.views.browse'),
    url(r'^browse/dish/[0-9]+$', 'website.views.browse'),

    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': path.join(path.dirname(__file__), 'static')}),
    # url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/static/'}),
)

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)