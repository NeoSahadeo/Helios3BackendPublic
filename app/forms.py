from django import forms
from .models import Password


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=255)
    password = forms.CharField(label='password', max_length=255)
