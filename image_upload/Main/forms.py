# forms.py 
from django import forms 
from .models import ImageUpload

class ImageUploadForm(forms.ModelForm): 
    class Meta: 
        model = ImageUpload 
        fields = ['source_image','checkprint_image'] 