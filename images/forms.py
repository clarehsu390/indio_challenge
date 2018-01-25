from django.forms import ModelForm
from .models import Image
from cloudinary.forms import CloudinaryFileField

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'