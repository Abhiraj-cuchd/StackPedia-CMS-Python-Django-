from django.forms import ModelForm
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UpdateProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
