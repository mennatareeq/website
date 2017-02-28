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
		for photo in Photo.objects.all():
			if len(objects_5)<5 :
				objects_5.append(photo)
			else:
				list_of_lists.append(objects_5)
				objects_5=[]
				objects_5.append(photo)
		if(len(objects_5)<5):
			list_of_lists.append(objects_5)
		print len(list_of_lists)
		for list in list_of_lists:
			print len(list)
		return list_of_lists





