from django.views import generic
from django.shortcuts import render
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from models import Photo
from django.http import HttpResponse


class Test(generic.DetailView):
	model = Photo
	template_name='photos/test.html'



def index(request):
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
	return render(request,'photos/index.html',{'list_of_lists':list_of_lists})





