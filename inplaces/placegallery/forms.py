from django import forms
from django.contrib.auth.models import User

from .models import UserProfile, Comment, InterestingPlace


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
        widgets = {
            'img_profile': forms.ClearableFileInput(attrs={'style': 'visibility: hidden; display: none'}),
        }


class UserComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PlaceForCheck(forms.ModelForm):
    class Meta:
        model = InterestingPlace
        fields = ['interesting_place_name_ru', 'city', 'street_name', 'house_number', 'description']
        widgets = {
            'interesting_place_name_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
            'street_name': forms.TextInput(attrs={'class': 'form-control'}),
            'house_number': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
