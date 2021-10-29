from django.db import models
from django.db.models.fields import CharField, PositiveSmallIntegerField

# Create your models here.
class Donor(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=10)
    age=models.PositiveSmallIntegerField()
    blood_group=models.CharField(max_length=3)
    date_last_donated=models.DateField(max_length=12,default=30,null=True)
    town=models.CharField(max_length=10,default=30,null=True)
    county=models.CharField(max_length=12,default=30,null=True)
    image=models.ImageField(upload_to="images/",null=True)
    phonenumber=models.CharField(max_length=30,null=True,blank=True)

  
