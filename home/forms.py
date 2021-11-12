from django import forms
from home.models import User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('id','username','first_name', 'last_name', 'email','image')