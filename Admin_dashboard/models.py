
from ast import Num
from venv import create
from django.db import models
from django.db import models

from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from django.views import View


########## Custom Model manager ########
class CustomUserManager(BaseUserManager):
    def create_user(self, name, email , phone_number, password):
        if not email:
            raise ValueError('The Email must be Set')
        if not name:
            raise ValueError("User Must have a name ")  
        user = self.model(
            email = self.normalize_email(email),
            name = name,
            phone_number = phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, name,phone_number,password):
        """
        Creates and saves a superuser with the given email, name, tc and password.
        """
        user = self.create_user(
            email = self.normalize_email(email),
            name = name,
            phone_number = phone_number,
            password = password, 
        )
        user.is_admin = True
        user.is_superuser = True
       
        user.save(using = self._db)
        return user    

############ Custom User Model ###########
class User(AbstractBaseUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(verbose_name = 'Email',max_length=255,unique=True)
    phone_number = models.CharField(max_length = 15, unique=True)
    is_active = models.BooleanField(default = True)
    is_admin = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CustomUserManager()


    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['name','phone_number']
    def __str__(self):
      return self.email
    def has_perm(self, perm, obj=None):
      "Does the user have a specific permission?"
      # Simplest possible answer: Yes, always
      return self.is_admin
    def has_module_perms(self, app_label):
      "Does the user have permissions to view the app `app_label`?"
      # Simplest possible answer: Yes, always
      return True

    @property
    def is_staff(self):
      "Is the user a member of staff?"
      # Simplest possible answer: All admins are staff
      return self.is_admin
  
  
  
  
########### Books Models ###############


class BooksModels(models.Model):
    book_name = models.CharField(max_length=100, null=True, blank=True)  
    auther = models.CharField(max_length=100, null=True, blank=True)  
    book_isbn = models.PositiveIntegerField(unique=True, null=False, blank=False)
    category = models.CharField(max_length=50, null=True, blank=True)
    created_date = models.DateField(auto_now_add=True, null=True, blank=True)
    
    
    
    