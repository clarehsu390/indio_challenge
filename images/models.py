# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from cloudinary.models import CloudinaryField

class Image(models.Model):
    name = models.CharField(max_length=200)
    photo = CloudinaryField('image')
    private = models.BooleanField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name

