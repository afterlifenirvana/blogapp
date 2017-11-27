# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.



class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about_him = models.TextField(max_length=500, blank=True)    

class Blog(models.Model):
    misc = 'Miscellaneous'
    tech = 'Technology'
    Category = ((tech, 'Technology'),(misc, 'Miscellaneous'))

    author = models.ForeignKey(Author)
    title = models.CharField(max_length=200, unique=True, blank=False)
    category = models.CharField(max_length=64, blank=False, choices=Category, default=tech)
    tags = models.CharField(max_length=200, blank=True)
    created_on = models.DateField(auto_now_add=True) 
    update_on = models.DateField(auto_now=True)
    published_on = models.DateField()
    short_summary = models.TextField(max_length=200, default=None, blank=False)
    content = RichTextUploadingField(blank=False)
    publish = models.BooleanField(default=False)
