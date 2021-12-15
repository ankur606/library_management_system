from django import forms
from django.db import models
from django.db.models.base import Model
from .models import Uploder

class ImageForm(forms.ModelForm):
    class Meta:
        model=Uploder
        field="__all__"