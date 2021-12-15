from django import forms
from django.db.models import fields

from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields="__all__"
        labels={'photo':'Select Image:'}