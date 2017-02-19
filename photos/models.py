from __future__ import unicode_literals
from django.db import models
#from django.core.files.storage import FileSystemStorage
# Create your models here.
#fs = FileSystemStorage(location='/media/photos')


class Photo(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to= '/media/photos')


#class Feature(models.Model):
#    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)