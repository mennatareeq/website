from __future__ import unicode_literals
from django.db import models

#from django.core.files.storage import FileSystemStorage
# Create your models here.
#fs = FileSystemStorage(location='/media/photos')

class ImageClass(models.Model):
    class_name= models.CharField(max_length=255)
    def __str__(self):
        return self.class_name


class Photo(models.Model):
    class_name = models.ForeignKey(ImageClass, on_delete=models.CASCADE)
    name        =   models.CharField(max_length=255)
    photo = models.ImageField(upload_to='./photos/media/photos/')
    features    =   models.FileField(blank = True , upload_to= './photos/media/features/')


    def __str__(self):
        return self.name


