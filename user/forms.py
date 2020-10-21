from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class my(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name",'username','email','password1','password2']
        
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Firstname'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Lastname'}),
            'username': forms.TextInput(attrs={'placeholder': 'Enter Your username'}),
            'email': forms.TextInput(attrs={'type':'email','placeholder': 'Enter Your Email'}),
            'password1': forms.PasswordInput(attrs={'type':'password','placeholder': 'Enter Your Password'}),
            'password2': forms.PasswordInput(attrs={'type':'password','placeholder': 'Confirm Your Password'}),
             
        }
 