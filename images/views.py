# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Image
from cloudinary.forms import cli_init_js_callbacks
from .forms import ImageForm
# Create your views here.
def index(request):
    images = Image.objects.all().order_by('created_at')
    context = {
        'images': images
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

def upload(request):
    context = dict( backend_form = ImageForm())

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        context['posted'] = form.instance
        if form.isvalid():
            form.save()
    return render(request, 'upload.html', context)

