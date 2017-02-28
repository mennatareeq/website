from django.views import generic
from django.shortcuts import render
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from models import Photo
from django.http import HttpResponse


class Test(generic.DetailView):
	model = Photo
	template_name='photos/test.html'


class IndexView(generic.ListView):
	template_name = 'photos/index.html'
	#context_object_name = 'all_photos'

	def get_queryset(self):
		list_of_lists=[]
		objects_5=[]
		i=0
		for photo in Photo.objects.all():
			if i<4 :
				objects_5.append(photo)
				i=i+1
			else:
				i=0
				list_of_lists.append(objects_5)
				del objects_5[:]
		return list_of_lists





