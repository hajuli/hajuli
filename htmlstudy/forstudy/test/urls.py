from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('forstudy.test',
    # Example:
    # (r'^forstudy/', include('forstudy.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
    
    (r'^MyHtml/$', 'MyHtml.index'),
    (r'^html2/', 'html2.index'),
    (r'^frameshtml/', 'frameshtml.index'),
)
