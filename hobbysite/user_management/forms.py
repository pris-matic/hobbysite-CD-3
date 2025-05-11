from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email']

class UserRegisterForm(UserCreationForm):
    name = forms.CharField(max_length=63, required=True)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username','name','password1', 'password2','email']