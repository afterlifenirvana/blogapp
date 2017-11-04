# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Blog(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200, unique=True)
    category = models.CharField(max_length=64)
    created_on = models.DateField(auto_now_add=True) 
    update_on = models.DateField(auto_now=True)
    published_on = models.DateField()
    short_summary = models.TextField()
    content = models.TextField()
    visible = models.BooleanField(default=False)
