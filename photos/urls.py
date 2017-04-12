from django.conf.urls import url
from . import views
from django.conf import settings
from django.views.generic import TemplateView

app_name = 'photos'

urlpatterns = [
	# /photos/
	url(r'^$', views.index , name='index'),

	# /photos/<photo_id>
	url(r'^(?P<pk>[0-9]+)$', views.Test.as_view(),  name='test'),

	#/photos/<class_id>
	url(r'^/$', views.search , name='search'),

]
