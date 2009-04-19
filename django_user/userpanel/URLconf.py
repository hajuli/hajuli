from django.conf.urls.defaults import *

# Myghtyboard URLs
urlpatterns = patterns('django_user.userpanel',
                       (r'^signup/$', 'views.signup'),
                       (r'^login/$', 'views.login'),
                       (r'^logout/$', 'views.logout'),
                       (r'^edit/$', 'views.edit'),
                       (r'^updatepswd/$', 'views.updatepswd'),
                       (r'^avatar/$', 'views.avatar'),
                       (r'^my_self/$', 'views.my_self'),
)
