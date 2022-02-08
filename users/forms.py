from dataclasses import fields
from django import forms
from django.contrib.auth.models import User, AbstractUser
from .models import Profile, Bio
from django.contrib.auth.forms import UserCreationForm
from ckeditor.fields import RichTextField

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name =forms.CharField(max_length=50)
    last_name =forms.CharField(max_length=50)


    class Meta:
        model =User
        fields = ['username', 'first_name', 'last_name','email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    # bio = RichTextField(blank =True, null =True)
   # bio = forms.TextField()
    class Meta:
        model =User
        fields = ['username', 'email',]

class ProfileUpdateForm(forms.ModelForm):
    class Meta :
        model =Profile
        fields =['image']

class BioUpdateForm (forms.ModelForm):
     class Meta:
        model = Bio
        fields = ['bio','location','birth_date']

