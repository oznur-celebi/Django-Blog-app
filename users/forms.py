from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    firstname =forms.CharField(max_length=20)
    surname =forms.CharField(max_length=20)


    class Meta:
        model =User
        fields = ['username', 'firstname', 'surname','email', 'password1', 'password2']