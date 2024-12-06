from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, ChoiceField, Select, SelectMultiple
from django.forms.widgets import ChoiceWidget
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError







class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class RegisterForm(UserCreationForm):

    class Meta:
        model=User
        fields = ['username', 'password1','password2']




