
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('djangotest',
    # Example:
    # (r'^forstudy/', include('forstudy.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
    
    (r'^home/', 'forstudy.home.index'),
    (r'^test/', include('forstudy.test.urls')),
    (r'^gg/', include('forstudy.gg.urls')),
    (r'^user_mgr/', include('user_mgr.views.urls'))
)
