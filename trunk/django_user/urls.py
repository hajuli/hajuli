from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

import settings

urlpatterns = patterns('',
    # Example:
    # (r'^django_user/', include('django_user.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
    (r'^hajuli/site_media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
#    (r'^user_mgr/', include('user_mgr.urls')),
    (r'^hajuli/userpanel/', include('userpanel.URLconf')),
    (r'^hajuli/$', 'userpanel.views.home'),
)
