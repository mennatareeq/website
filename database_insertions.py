import os
from photos.models import Photo
from django.core.files import File

directory = "/home/manar/Downloads/Coverup/"

images = []
files = []
for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        images.append(filename)
    elif filename.endswith(".txt"):
        files.append(filename)

images.sort()
files.sort()
print number
for i in range(number):
    ph = Photo()
    ph.name = images[i]
    ph.photo.save(images[i], File(open('/home/asmaanabil/from_here/2.jpg', 'r')))
    ph.featuers.save(files[i], File(open('/home/asmaanabil/from_here/index.csv', 'r')))
