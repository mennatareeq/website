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
from cart.forms import CartAddProductForm


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

def Index(request):
	photos=Photo.objects.all()
	cart_product_form = CartAddProductForm()
	return render(request,'photos/index.html',{'photos':photos,'cart_product_form': cart_product_form})


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























