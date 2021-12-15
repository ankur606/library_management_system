from django.db import models

# Create your models here.
class Uploder(models.Model):
    img=models.ImageField(upload_to="myimage")