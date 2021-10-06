from django import forms
from django.contrib.auth.models import User


class UserLogin(forms.ModelForm):
    nickname = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=50)

    class Meta:
        model = User


class UserRegister(forms.ModelForm):
    nickname = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=50)
    password_repeat = forms.CharField(widget=forms.PasswordInput(), max_length=50)

    class Meta:
        model = User
