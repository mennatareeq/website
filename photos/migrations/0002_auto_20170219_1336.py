# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 11:36
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/photos'), upload_to=b''),
        ),
    ]