from django.forms import ModelForm, widgets
from django import forms

from cart.models import CartAddress


class CartAddressForm(ModelForm):
    class Meta:
        model = CartAddress
        exclude = ['id', 'cart_id']
        widgets = {
            'full_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'street_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'house_number': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'postal_code': widgets.TextInput(attrs={'class': 'form-control'}),
        }