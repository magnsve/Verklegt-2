from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from products.forms.product_form import ProductUpdateForm, ProductCreateForm, ProdcutCategoryCreateForm, \
    ProductManufacturerCreateForm, ProductManufacturerUpdateForm, ProductCategoryUpdateForm
from products.models import Product, ProductManufacturer, ProductCategory, ProductImage
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


@login_required
@admin_required
def administrate_manufacturers(request):
    context = {'manufacturers': ProductManufacturer.objects.all().order_by('name')}
    return render(request, 'administrate/administrate_manufacturers.html', context)


@login_required
@admin_required
def administrate_categories(request):
    context = {'categories': ProductCategory.objects.all().order_by('name')}
    return render(request, 'administrate/administrate_categories.html', context)


@login_required
@admin_required
def product_products(request):
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'administrate/all_products.html', context)


@login_required
@admin_required
def get_product_by_id(request, id):
    return render(request, 'administrate/product_details.html', {
        'product': get_object_or_404(Product, pk=id)
    })


@login_required
@admin_required
def create_product(request):
    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)
        if form.is_valid():
            product = form.save()
            product_image = ProductImage(image=request.POST['image'], product=product)
            product_image.save()
            return redirect('products_products')
    else:
        form = ProductCreateForm()
    return render(request, 'products/create_product.html', {
        'form': form
    })


@login_required
@admin_required
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('products_products')


@login_required
@admin_required
def update_product(request, id):
    instance = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        form = ProductUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('products_products')
    else:
        form = ProductUpdateForm(instance=instance)
    return render(request, 'administrate/update_product.html', {
        'form': form,
        'id': id
    })


@login_required
@admin_required
def create_manufacturer(request):
    if request.method == 'POST':
        form = ProductManufacturerCreateForm(data=request.POST)
        if form.is_valid():
            manufacturer = form.save()
            return redirect('administrate_products')
    else:
        form = ProductManufacturerCreateForm()
    return render(request, 'administrate/administrate_manufacturers.html', {
        'form': form
    })


@login_required
@admin_required
def update_manufacturer(request, id):
    instance = get_object_or_404(ProductManufacturer, pk=id)
    if request.method == 'POST':
        form = ProductManufacturerUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('products_manufacturers')
    else:
        form = ProductManufacturerUpdateForm(instance=instance)
    return render(request, 'administrate/update_manufacturer.html', {
        'form': form,
        'id': id
    })


@login_required
@admin_required
def delete_manufacturer(request, id):
    manufacturer = get_object_or_404(ProductManufacturer, pk=id)
    manufacturer.delete()
    return redirect('products_manufacturers')


@login_required
@admin_required
def create_category(request):
    if request.method == 'POST':
        form = ProdcutCategoryCreateForm(data=request.POST)
        if form.is_valid():
            category = form.save()
            return redirect('product-index')
    else:
        form = ProdcutCategoryCreateForm()
    return render(request, 'products/create_category.html', {
        'form': form
    })


@login_required
@admin_required
def update_category(request, id):
    instance = get_object_or_404(ProductCategory, pk=id)
    if request.method == 'POST':
        form = ProductCategoryUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('products_categories')
    else:
        form = ProductCategoryUpdateForm(instance=instance)
    return render(request, 'administrate/update_categories.html', {
        'form': form,
        'id': id
    })


@login_required
@admin_required
def delete_category(request, id):
    category = get_object_or_404(ProductCategory, pk=id)
    category.delete()
    return redirect('products_categories')


@login_required
@admin_required
def update_product(request, id):
    instance = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        form = ProductUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('product_details', id=id)
    else:
        form = ProductUpdateForm(instance=instance)
    return render(request, 'administrate/update_product.html', {
        'form': form,
        'id': id
    })