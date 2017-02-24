from django.views import generic
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from models import Photo

class IndexView(generic.ListView):
	template_name = 'photos/index.html'
	context_object_name = 'all_photos'

	def get_queryset(self):
		return Photo.objects.all()
