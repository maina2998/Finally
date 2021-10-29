from django import forms
from .models import Donor

class donorRegistrationForm(forms.ModelForm):
    class Meta:
        model=Donor
        fields="__all__"