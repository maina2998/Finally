from django import forms
from django.forms import fields, models
from .models import Recipient

class RecipientRegistrationForm(forms.ModelForm):
    class Meta:
        model=Recipient
        fields="__all__"