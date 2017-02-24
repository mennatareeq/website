from django.conf.urls import url
from . import views #eldot m3naha from this folder

# 4akl el urlpattern bykon:
#	2wel operand hwa el regular exprestion elly ba7ot feh el url elly hyetketeb
#	eltany hwa elpath llresponce 3la el url request da, views.index msln fa keda index de function fe views bet3emel task mo3yna
#	eltalta lesa mo43arfa

app_name = 'photos'

urlpatterns = [
	# /photos/
	url(r'^$', views.IndexView.as_view() , name='index'),
]
