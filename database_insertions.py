import os
from photos.models import Photo, ImageClass
from django.core.files import File

images_directory = '/home/asmaanabil/Downloads/mini-dataset'
features_directory = '/home/asmaanabil/Downloads/mini-dataset2'

for root, dirs, files in os.walk(images_directory):

    for direcory in dirs:
        image_class = ImageClass()
        image_class.class_name=direcory.lower()

        images_dir= images_directory+'/'+direcory
        if os.listdir(images_dir):
            image_class.save()
            print 'class ' + direcory + ' is added to database'
            for filee in os.listdir(images_dir):
                if filee.endswith('.jpg'):
                    ph = Photo()
                    ph.name = filee
                    ph.class_name=image_class
                    ph.photo.save(filee, File(open(images_dir+'/' + filee, 'r')))
                    feature_file_dir= features_directory+'/'+direcory+'/'+filee+'.txt'
                    ph.features.save(filee, File(open(feature_file_dir, 'r')))
                    ph.save()

