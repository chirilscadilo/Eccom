from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegistration(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']

        labels = {
            'first_name': 'Name',
            'email':'Email',
            'username': 'Username',
            'password1': 'Your Password',
            'password2': 'Confirm Password',
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile

        fields = ['name', 'email', 'username']

        labels = {
            'name': 'Name',
            'email': 'Email',
            'username': 'Username',
        }