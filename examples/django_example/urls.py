from django.conf.urls.defaults import *
import cereal

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^django_example/', include('django_example.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
	(r'^$', 'django.views.generic.simple.direct_to_template',
		{'template':'index.html'}),
	(r'^api/', include(cereal.urls)),
)
