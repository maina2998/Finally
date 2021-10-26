from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import CharField, PositiveSmallIntegerField
# from phonenumber_field.modelfields import PhoneNumberField


class Appeals(models.Model):
    first_name = models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    blood_group=models.CharField(max_length=3)
    # Phone_number=models.PhoneNumberField(unique=True)
    county=models.CharField(max_length=100)
    town=models.CharField(max_length=100)
    date_last_donated=models.DateField()
    age=PositiveSmallIntegerField()
    



    

