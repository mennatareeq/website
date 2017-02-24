from django.views import generic
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from models import Photo
from django.http import HttpResponse


class Test(generic.DetailView):
	model = Photo
	template_name='photos/test.html'


class IndexView(generic.ListView):
	template_name = 'photos/index.html'
	context_object_name = 'all_photos'

	def get_queryset(self):
		return Photo.objects.all()




