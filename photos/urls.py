from django.conf.urls import url
from . import views #eldot m3naha from this folder
from django.conf import settings

app_name = 'photos'

urlpatterns = [
	# /photos/
	url(r'^$', views.IndexView.as_view()  , {'document_root': settings.PHOTOS_ROOT} , name='index'),
]
