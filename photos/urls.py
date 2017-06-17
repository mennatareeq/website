from django.conf.urls import url
from . import views
from django.conf import settings
from django.views.generic import TemplateView

app_name = 'photos'

urlpatterns = [
	# /photos/
	url(r'^$', views.Index , name='index'),

	# /photos/<photo_id>
	url(r'^(?P<pk>[0-9]+)$', views.Test.as_view(),  name='test'),

	#/photos/search-results/
	url(r'^search-results/$', views.search , name='search'),

	#/photos/<class_id>
	url(r'^(?P<id>[0-9]+)/$', views.search_buttons , name='search_buttons'),

]
