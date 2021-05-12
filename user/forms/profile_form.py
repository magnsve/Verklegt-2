from django import forms
from django.forms import ModelForm, widgets
from user.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user', 'admin']
        widgets = {
            'bio': widgets.TextInput(attrs={'class': 'form-control'}),
            'profile_image': widgets.TextInput(attrs={'class': 'form-control'})
        }


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'profile_image', 'user', 'bio']
        widgets = {
            'admin': widgets.CheckboxInput(attrs={'class': 'checkbox'})
        }