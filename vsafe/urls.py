from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from website import views

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
    url(r'^$', views.index),
    url(r'^learn/?$', views.learn),
    url(r'^browse/?$', views.index),
    url(r'^browse/ingredient/(?P<id_num>[0-9]+)/?$', views.ingredient),
    url(r'^browse/dish/(?P<id_num>[0-9]+)/?$', views.dish),
    url(r'^browse/subset/', views.subset),
    url(r'^list_all/', views.list_all),
)