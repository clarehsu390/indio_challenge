# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Image
from .forms import ImageForm
# Create your views here.
def index(request):
    images = Image.objects.all().order_by('created_at')
    return render(request, 'index.html', dict(images=images))

def upload(request):
    context = dict( backend_form = ImageForm())

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        context['posted'] = form.instance
        if form.is_valid():
            form.save()
    return render(request, 'upload.html', context)

