<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from cart.forms.cart_form import CartAddressForm, CartUpdateForm
from cart.models import Cart, CartAddress, CartItems
from products.models import Product


def index(request):
    cart = Cart.objects.all().filter(profile_id=request.user.profile.id).filter(is_open=True).first()
    if not cart:
        cart = Cart(profile_id=request.user.profile.id)
        cart.save()
    cart_items = CartItems.objects.all().filter(cart_id=cart.id)
    context = {'cart': cart_items}
    return render(request, 'cart/index.html', context)

@login_required
def add_to_cart(request, id):
    cart = Cart.objects.all().filter(profile_id=request.user.profile.id).filter(is_open=True).first()
    if not cart:
        cart = Cart(profile_id=request.user.profile.id)
        cart.save()
    product = get_object_or_404(Product, pk=id)
    is_product_in_cart = CartItems.objects.all().filter(cart_id=cart.id).filter(product_id=product.id)
    if not is_product_in_cart:
        newline = CartItems(cart_id=cart.id, product_id=product.id, quantity=1, total_price=product.price)
        newline.save()
    cart_items = CartItems.objects.all().filter(cart_id=cart.id)
    context = {'cart': cart_items}
    return render(request, 'cart/index.html', context)

@login_required
def contact(request):
    profile_id = request.user.profile.id
    cart = Cart.objects.filter(profile_id=profile_id).filter(is_open=True)
    contact_info = CartAddress.objects.filter(cart_id=cart.id)
    form = CartAddressForm(data=request.POST)
    return render(request, 'cart/index.html')
=======
from django.shortcuts import render


def index(request):
    return render(request, 'cart/index.html')
>>>>>>> e1b9061 (Forsíða)
