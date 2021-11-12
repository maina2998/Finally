from django.db import models
from django.contrib.auth.models import User #add this

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username=models.CharField(max_length=20,null=True,blank=True)
    first_name=models.CharField(max_length=20,null=True,blank=True)
    last_name=models.CharField(max_length=20,null=True,blank=True)
    email=models.EmailField(max_length=50,null=True,blank=True)
    # image=models.ImageField(default="redswift/static/images/logo2.jpg1" , upload_to="images/",null=True)
    superusers = User.objects.filter(is_superuser=True)

