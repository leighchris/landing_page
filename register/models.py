from django.db import models
#from django.contrib.auth.models import AbstractUser, UserManager



# Create your models here.

class Register(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    
    
##class Profile(models.Model):
##    user = models.OneToOneField(User, on_delete = models.CASCADE)
##    title = models.CharField(max_length = 50)
##    location = models.CharField(max_length = 30, blank = True)
##    bio = models.TextField(max_length = 500, blank = True)
#
#class CustomUserManager(UserManager):
#    pass
#
#class CustomUser(AbstractUser):
#    custom_user = CustomUserManager()
#    title = models.CharField(max_length = 50)
#    location = models.CharField(max_length = 30, blank = True)
#    bio = models.TextField(max_length = 500, blank = True)

    
