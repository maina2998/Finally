from django.db import models


from django.contrib.auth.models import User #add this

# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=20,null=True,blank=True)
    first_name=models.CharField(max_length=20,null=True,blank=True)
    last_name=models.CharField(max_length=20,null=True,blank=True)
    email=models.EmailField(max_length=50,null=True,blank=True)


    superusers = User.objects.filter(is_superuser=True)
class Profile(models.Model):   #add this class and the following fields
    user = models.ManyToManyField(User, max_length=50)

