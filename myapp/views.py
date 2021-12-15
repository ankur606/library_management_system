from django import forms
from django.shortcuts import render
from .forms import ImageForm
from .models import Image

# Create your views here.
def about(request):
    return render(request,"about.html")
def home(request):
    form=ImageForm()
    if request.method=="POST":
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form=ImageForm()   
    img=Image.objects.all()  
    return render(request,'Imageuploder/home.html',{'img':img,'form':form})
def my(request):
    return render(request,'Imageuploder/my.html')