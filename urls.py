from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^delish/', include('codeandbeer.delish.urls')),
	(r'^delish/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/neypalm/Code/Python/Django/codeandbeer/templates/delish/media'}),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/', include(admin.site.urls)),
)
