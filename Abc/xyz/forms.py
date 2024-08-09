from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username=forms.CharField(label="Username", widget=forms.TextInput(
        attrs={
            'placeholder':'akash001',
            'class': 'form-control'
        }
    ))
    first_name=forms.CharField(label="First Name", widget=forms.TextInput(
        attrs={
            'placeholder': 'Akash',
            'class':  'form-control'
        }
    ))
    last_name=forms.CharField(label="Last Name", widget=forms.TextInput(
        attrs={
            'placeholder': 'Gupta',
            'class':  'form-control'
        }
    ))
    email=forms.CharField(label="Email", widget=forms.TextInput(
        attrs={
            'placeholder': 'akash@gmail.com',
            'class':  'form-control'
        }
    ))
    password1=forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={
            'placeholder': 'password',
            'class':  'form-control'
        }
    ))
    password2=forms.CharField(label="Re-Enter Password", widget=forms.PasswordInput(
        attrs={
            'placeholder': 'password',
            'class':  'form-control'
        }
    ))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

class SignInForm(AuthenticationForm):
    username=forms.CharField(label="Username", widget=forms.TextInput(
        attrs={
            'placeholder':'akash001',
            'class': 'form-control'
        }
    ))
    password=forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={
            'placeholder': 'password',
            'class':  'form-control'
        }
    ))