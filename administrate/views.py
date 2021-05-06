from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from products.forms.product_form import ProductUpdateForm
from products.models import Product
from ship_o_cereal.decorators import admin_required
from user.models import Profile


@login_required
@admin_required
def index(request):
    return render(request, 'administrate/index.html')


@login_required
@admin_required
def administrate_products(request):
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'administrate/administrate_products.html', context)


@login_required
@admin_required
def get_product_by_id(request, id):
    return render(request, 'products/product_details.html', {
        'product': get_object_or_404(Product, pk=id)
    })


@login_required
@admin_required
def update_product(request, id):
    instance = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        form = ProductUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('administrate_product', id=id)
    else:
        form = ProductUpdateForm(instance=instance)
    return render(request, 'administrate/single_product.html', {
        'form': form,
        'id': id
    })


@login_required
@admin_required
def administrate_users(request):
    context = {'profiles': Profile.objects.exclude(id=request.user.profile.id)}
    return render(request, 'administrate/administrate_users.html', context)


@login_required
@admin_required
def toggle_admin(request, id):
    profile = get_object_or_404(Profile, pk=id)
    profile.admin = not profile.admin
    profile.save()
    return redirect('administrate_users')