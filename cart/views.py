from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from cart.forms.cart_form import CartAddressForm
from cart.models import Cart, CartAddress


def index(request):
    return render(request, 'cart/index.html')


@login_required
def contact(request):
    profile_id = request.user.profile.id
    cart = Cart.objects.filter(profile_id=profile_id).filter(is_open=True)
    contact_info = CartAddress.objects.filter(cart_id=cart.id)
    form = CartAddressForm(data=request.POST)
    return render(request, 'cart/index.html')