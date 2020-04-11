from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
"""
for="inputEmail"
for="inputPhone"
for="inputAddress"
for="inputPassword"
for="inputConfirmPassword"
"""

class RegisterForm(UserCreationForm):
    username = forms.CharField( widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder':'Username',
            'type' : 'text',
            'id' : 'username'
        }
    ))
    name = forms.CharField( widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder':'Name',
            'type' : 'text',
            'id' : 'name'
        }
    ))
    email = forms.EmailField( widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder':'Email',
            'type' : 'text',
            'id' : 'email'
        }
    ))
    phone = forms.CharField( widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder':'Username',
            'type' : 'text',
            'id' : 'phone'
        }
    ))
    address = forms.CharField( widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder':'Username',
            'type' : 'text',
            'id' : 'address'
        }
    ))
    password1 = forms.CharField( widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id' : 'password',

        }
    ))
    password2 = forms.CharField( widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Password',
            'id' : 'password2'
        }
    ))
    class Meta:
        model = User
        fields = ( 'username' , 'email' , 'name' , 'phone' , 'address', 'password1', 'password2')

