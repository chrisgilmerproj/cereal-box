from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
	('^(?P<model>\w+)/(?P<function>\w+)', views.json_api)
)
