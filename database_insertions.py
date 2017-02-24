import os
from photos.models import Photo
from django.core.files import File

directory = '/home/manar/Downloads/Coverup/'

images = []
files = []
for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        images.append(filename)
    elif filename.endswith(".txt"):
        files.append(filename)

images.sort()
files.sort()
number=len(images)
for i in range(number):
    ph = Photo()
    ph.name = images[i]
    ph.photo.save(images[i], File(open(directory+images[i], 'r')))
    ph.features.save(files[i], File(open(directory+files[i], 'r')))
