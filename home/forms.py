from django import forms
from home.models import Profile,User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')
      
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user',)    