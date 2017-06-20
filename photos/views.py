from django.views import generic
from django.shortcuts import render , redirect
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from models import Photo , ImageClass , LabelsClass
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

'''
images_dir = '/home/asmaanabil/Desktop/test2/'
modelFullPath = '/home/asmaanabil/Downloads/inception-2015-12-05/classify_image_graph_def.pb'
indexpath = '/home/asmaanabil/Desktop/featureswaleed.csv'
list_images = [images_dir + f for f in os.listdir(images_dir) if re.search('jpg|JPG', f)]
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
'''


class Test(generic.DetailView):
	model = Photo
	template_name='photos/test.html'

def Index(request):
	photos=Photo.objects.all()
	cart_product_form = CartAddProductForm()
	return render(request,'photos/index.html',{'photos':photos,'cart_product_form': cart_product_form})


all_classes_names = []
all_classes = ImageClass.objects.all()
for classX in all_classes:
	all_classes_names.append(classX.class_name)

all_labels_names = []
all_labels = LabelsClass.objects.all()
for label in all_labels:
	all_labels_names.append(label.label_name)


# def get_labels_for_classX(classX):
# 	related_labels = []
# 	for image_class in ImageClass.objects.all():
# 		if image_class.class_name == classX.lower():
# 			related_images = image_class.photo_set.all()
# 			for image in related_images:
# 				labels = list(image.label_name.all())
# 				for label in labels:
# 					related_labels.append(label)
#
# 	return 	list(set(related_labels))

def get_all_images(name , type):
	if type == 'class':
		related_images = []
		for image_class in ImageClass.objects.all():
			if image_class.class_name == name.lower():
				related_images = image_class.photo_set.all()
				break
	if type == 'label':
		related_images = []
		for image_label in LabelsClass.objects.all():
			if image_label.label_name == name.lower():
				related_images = image_label.photo_set.all()
				break

	return related_images

def search(request):
	# suggested_labels = []
	list_for_each_word = []
	related_images = []
	empty = 1
	if request.method == "POST":
		search_text = request.POST.get("input")
		search_words = search_text.split()

		for i in range(0 , len(search_words)):
			if search_words[i] in all_labels_names:
				empty = 0

				three_words_label = search_words[i]
				two_words_label = search_words[i]

				if len(search_words) > i+3:
					three_words_label= search_words[i]+' '+search_words[i+1]+' '+search_words[i+2]
				elif len(search_words) > i+2 :
					two_words_label = search_words[i]+' '+search_words[i+1]

				if three_words_label in all_labels_names:
					related_images = get_all_images(three_words_label , 'label')
					i += 3
				elif two_words_label in all_labels_names:
					related_images = get_all_images(two_words_label, 'label')
					i += 2
				else:
					related_images = get_all_images(search_words[i] , 'label')

				if len(related_images) != 0:
					list_for_each_word.append(related_images)

			elif search_words[i] in all_classes_names:
				empty = 0
				# suggested_labels = get_labels_for_classX(search_words[i])
				related_images = get_all_images(search_words[i] , 'class')
				if len(related_images) != 0:
					list_for_each_word.append(related_images)

		if len(list_for_each_word) != 0:
			related_images = set(list_for_each_word[0])
			for s in list_for_each_word[1:]:
				related_images.intersection_update(s)


	return render(request, 'photos/search.html' , {'related_images':related_images,
												   'empty':empty , 'all_classes': ImageClass.objects.all()})

def search_buttons(request , id):
	classX = ImageClass.objects.filter(id=id).first()
	images = get_all_images(classX.class_name , 'class')
	return render(request , 'photos/show_classX_images.html' , {'related_images':images})

# def suggested_labels_buttons(request , label_id , class_id):
# 	return

























