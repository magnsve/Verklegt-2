from django.forms import ModelForm, widgets
from django import forms
from cart.models import CartAddress, CartItems


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


class CartUpdateForm(ModelForm):
    class Meta:
        model = CartItems
        exclude = ['id', 'cart_id']
        widgets = {
            'product': widgets.TextInput(attrs={'class': 'form-control'}),
            'quantity': widgets.TextInput(attrs={'class': 'form-control'}),
            'total_price': widgets.TextInput(attrs={'class': 'form-control'}),
        }


