from django.views import generic
from django.shortcuts import render
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from models import Photo
from django.http import HttpResponse


class Test(generic.DetailView):
	model = Photo
	template_name='photos/test.html'


def index(request):
	#template_name = 'photos/index.html'
	context_object_name = 'all_photos'
	list_of_lists=[]
	objects_5=[]
	i=0
	for photo in Photo.objects.all():
		if i<4 :
			objects_5.append(photo)
		else:
			list_of_lists.append(objects_5)
			del objects_5[:]
	return render(request,'photos/index.html' ,{'list_of_lists':list_of_lists})





