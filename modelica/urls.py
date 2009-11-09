from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^modelica/', include('modelica.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^newsletter/\d+/images/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_DOC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    (r'^images/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_DOC_ROOT}),
    (r'^newsletter/$', 'modelica.newsletter.views.index'),
    (r'^newsletter/(?P<id>\d+)/$', 'modelica.newsletter.views.render'),
    (r'^newsletter/(?P<id>\d+)/upload$', 'modelica.newsletter.views.upload_fs'),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
