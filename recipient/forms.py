from django import forms
from django.forms import fields, models
from .models import Recipient

class RecipientRegistrationForm(forms.ModelForm):#ModelForm converts recipient model into a django form
    class Meta:
        model=Recipient
        fields="__all__"