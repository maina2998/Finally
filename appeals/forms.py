from django import forms
from django.db import models
from django.forms import fields
from .models import Appeals
from django.db.models.fields.files import ImageField

class Addappealforms(forms.ModelForm):
    class Meta:
        model=Appeals
        fields="__all__"