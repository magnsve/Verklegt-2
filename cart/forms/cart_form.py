from django.forms import ModelForm, widgets, inlineformset_factory
from cart.models import CartAddress, CartItems, Cart
from django import forms


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


class CartItemsUpdateForm(ModelForm):
    class Meta:
        model = CartItems
        exclude = ('id', 'product')
        widgets = {
            'product_name': widgets.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'quantity': widgets.NumberInput(attrs={'class': 'form-control'}),
            'total_price': widgets.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'})
        }
