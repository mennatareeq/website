from django.views import generic
from django.shortcuts import render , redirect
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from models import Photo , ImageClass
from django.http import HttpResponse
import numpy as np
import tensorflow as tf
import argparse
import glob
import os
import re
from tensorflow.python.platform import gfile
import csv
from django.contrib.auth import authenticate , login
from django.views.generic import View
from django.contrib.auth.models import User


'''images_dir = '/home/asmaanabil/Desktop/test2/'
modelFullPath = '/home/asmaanabil/Downloads/inception-2015-12-05/classify_image_graph_def.pb'
indexpath = '/home/asmaanabil/Desktop/featureswaleed.csv'
list_images = [images_dir + f for f in os.listdir(images_dir) if re.search('jpg|JPG', f)]'''
def create_graph():
	"""Creates a graph from saved GraphDef file and returns a saver."""
	# Creates graph from saved graph_def.pb.
	with tf.gfile.FastGFile(modelFullPath, 'rb') as f:
		graph_def = tf.GraphDef()
		graph_def.ParseFromString(f.read())
		_ = tf.import_graph_def(graph_def, name='')
def extract_features(list_images):
	nb_features = 2048
	features = np.empty((len(list_images), nb_features))
	labels = []
	create_graph()
	with tf.Session() as sess:
		next_to_last_tensor = sess.graph.get_tensor_by_name('pool_3:0')
		output = open(indexpath, "w")
		for ind, image in enumerate(list_images):
			print('Processing %s...' % (image))
			if not gfile.Exists(image):
				tf.logging.fatal('File does not exist %s', image)
			image_data = gfile.FastGFile(image, 'rb').read()  ##
			predictions = sess.run(next_to_last_tensor,
								   {'DecodeJpeg/contents:0': image_data})
			feature = np.squeeze(predictions)
			feature = [str(f) for f in feature]
			output.write("%s,%s\n" % (image, ",".join(feature)))
			features[ind, :] = feature
		# labels.append(re.split('_\d+',image.split('/')[1])[0])
		return features
		output.close()



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

def search(request):
	related_images = ImageClass().photo_set.all()
	input_text = ""
	if request.method == "POST":
		input_text = request.POST.get("input")
		for image_class in ImageClass.objects.all():
			if image_class.class_name == input_text.lower() :
				related_images = image_class.photo_set.all()
				break
	return render(request, 'photos/search.html' , {'input_text' : input_text , 'related_images':related_images })

'''class UserFormView(View):
	form_class = UserForm
	template_name = 'photos/registration_form.html'

	# display blank form
	def get(self , request):
		form = self.form_class(None)
		return render(request , self.template_name , {'form':form})

	# process form data
	def post(self , request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False) #create an object from the form but not save

			#cleaned normalized data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			# return user objects if credentials are correct
			user = authenticate(username=username , password=password)

			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect('photos:index')

		return render(request, self.template_name, {'form': form})'''

'''def register(request):
	return render(request ,  'photos/registration_form.html' )

def signup(request):
	#new_user = UserAccount()
    user = User()
    if request.method == "POST":
        user = User.objects.create_user( request.POST.get("username"), irequest.POST.get("email"), request.POST.get("password"))
		#new_user.username = request.POST.get("username")
		#new_user.password = request.POST.get("password")
		#new_user.email = irequest.POST.get("email")
		#new_user.save()

	return render(request , 'photos/index.html' )'''






















