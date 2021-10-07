from django import forms
from django.contrib.auth.models import User

from .models import UserProfile


class UserBaseSettings(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class UserAdditionalSettings(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['img_profile']
