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
        exclude = ['id']
        widgets = {
            'bio': widgets.TextInput(attrs={'class': 'form-control'}),
            'profile_image': widgets.TextInput(attrs={'class': 'form-control'}),
            'admin': widgets.CheckboxInput(attrs={'class': 'checkbox'})
        }