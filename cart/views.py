from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from cart.forms.cart_form import CartAddressUpdateForm, CartPaymentUpdateForm
from cart.models import Cart, CartAddress, CartItems, CartPayment
from products.models import Product


@login_required
def increase_by_one(request, id):
    item = get_object_or_404(CartItems, pk=id)
    print(item.quantity)
    item.quantity = item.quantity + 1
    item.save()
    print(item.quantity)
    return redirect('cart-index')


@login_required
def decrease_by_one(request, id):
    item = get_object_or_404(CartItems, pk=id)
    item.quantity = item.quantity - 1
    if item.quantity == 0:
        item.delete()
    else:
        item.save()
    return redirect('cart-index')


@login_required
def index(request):
    cart = Cart.objects.all().filter(profile_id=request.user.profile.id).filter(is_open=True).first()
    if not cart:
        cart = Cart(profile_id=request.user.profile.id)
        cart.save()
        address = CartAddress(cart_id=cart.id)
        address.save()
        payment = CartPayment(cart_id=cart.id)
        payment.save()
    cart_items = CartItems.objects.all().filter(cart_id=cart.id)
    total = 0
    for cart_item in cart_items:
        if cart_item.quantity == 0:
            cart_item.delete()
        else:
            product = Product.objects.all().filter(id=cart_item.product_id).first()
            total_price = cart_item.quantity * int(product.price)
            cart_item.total_price = total_price
            cart_item.save()
            total = total + cart_item.total_price
    context = {
        'cart': cart_items,
        'total': total
    }
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
        newline = CartItems(cart_id=cart.id, product_id=product.id, product_name=product.name, quantity=1, total_price=product.price)
        newline.save()
    return redirect('cart-index')


@login_required
def contact(request):
    cart = Cart.objects.all().filter(profile_id=request.user.profile.id).filter(is_open=True).first()
    try:
        instance = CartAddress.objects.all().filter(cart_id=cart.id).first()
        if request.method == 'POST':
            form = CartAddressUpdateForm(data=request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('contact')
        else:
            form = CartAddressUpdateForm(instance=instance)
    except:
        if request.method == 'POST':
            form = CartAddressUpdateForm(data=request.POST)
            if form.is_valid():
                address = form.save(commit=False)
                address.cart_id = cart.id
                address.save()
                return redirect('contact')
        else:
            form = CartAddressUpdateForm()
    return render(request, 'cart/contact.html', {'form': form})


@login_required
def payment(request):
    cart = Cart.objects.all().filter(profile_id=request.user.profile.id).filter(is_open=True).first()
    try:
        instance = CartPayment.objects.all().filter(cart_id=cart.id).first()
        if not instance:
            raise Exception
        if request.method == 'POST':
            form = CartPaymentUpdateForm(data=request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('contact')
        else:
            form = CartPaymentUpdateForm(instance=instance)
    except:
        if request.method == 'POST':
            form = CartPaymentUpdateForm(data=request.POST)
            if form.is_valid():
                payment_object = form.save(commit=False)
                payment_object.cart_id = cart.id
                payment_object.save()
                return redirect('contact')
        else:
            form = CartPaymentUpdateForm()
    return render(request, 'cart/payment.html', {'form': form})


@login_required
def review(request):
    cart = Cart.objects.all().filter(profile_id=request.user.profile.id).filter(is_open=True).first()
    payment_step = CartPayment.objects.all().filter(cart_id=cart.id).first()
    contact_step = CartAddress.objects.all().filter(cart_id=cart.id).first()
    context = {
        'payment_step': payment_step,
        'contact_step': contact_step
    }
    return render(request, 'cart/review.html', context)

@login_required
def confirmation(request):
    cart = Cart.objects.all().filter(profile_id=request.user.profile.id).filter(is_open=True).first()
    cart.is_open = False
    cart.save()
    return render(request, 'cart/confirmation.html')