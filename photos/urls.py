from django.conf.urls import url
from . import views
from django.conf import settings
from django.views.generic import TemplateView

app_name = 'photos'

urlpatterns = [
	# /photos/
	url(r'^$', views.Index.as_view() , name='index'),

	# /photos/register/
	#url(r'^register/$', views.register , name='register'),

	# /photos/<photo_id>
	url(r'^(?P<pk>[0-9]+)$', views.Test.as_view(),  name='test'),

	#/photos/<class_id>
	url(r'^$', views.search , name='search'),

	# /photos/
	#url(r'^$', views.signup , name='signup'),

]
