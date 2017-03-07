from django.conf.urls import url
from . import views #eldot m3naha from this folder
from django.conf import settings

app_name = 'photos'

urlpatterns = [
	# /photos/
	url(r'^$', views.index , name='index'),

	# /photos/<photo_id>
	url(r'^(?P<pk>[0-9]+)$', views.Test.as_view(),  name='test'),

	#/photos/result

]
