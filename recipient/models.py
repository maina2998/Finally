from django.db import models
from django.db.models.fields import CharField, PositiveSmallIntegerField

# Create your models here.
class Recipient(models.Model):
    first_name=models.CharField(max_length=20,default=None)
    last_name=models.CharField(max_length=20,default=None)
    age=models.PositiveSmallIntegerField(default=None)
    hospital=models.CharField(max_length=50,default=None)
    ward=models.CharField(max_length=30,null=True)
    location=models.CharField(max_length=100,default=None,blank=True,null=True)
    blood_group=models.CharField(max_length=3,default=None,blank=True,null=True)
    blood_pints=models.CharField(max_length=10,default=None,blank=True,null=True)
    contact_person=models.CharField(max_length=100,default=None,blank=True,null=True)
    # contact_person_phonenumber=models.CharField(max_length=30,null=True,blank=True)
    date=models.DateField(auto_now=True, null=True)
