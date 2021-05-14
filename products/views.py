from datetime import timedelta, date
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from products.forms.product_form import ProductCreateForm, ProdcutCategoryCreateForm, ProductManufacturerCreateForm
from products.models import Product, ProductImage, ProductCategory
from ship_o_cereal.decorators import admin_required
from user.models import SearchHistory

#Index for search and search history
def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        products = [ {
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search_filter)]
        if request.user.is_authenticated:
            try:
                _ = SearchHistory.objects.create(profile=request.user.profile, search_string=search_filter)
            except:
                pass
        return JsonResponse({ 'data': products })
    today = date.today()
    yesterday = today - timedelta(1)
    lastweek = today - timedelta(7)
    sort_by = request.GET.get('sort', 'name')
    if sort_by not in ['name', '-name', 'category', '-category', 'price', '-price']:
        sort_by = 'name'
    categories = ProductCategory.objects.all().order_by('name')
    filter_by = request.GET.get('category', 'all')
    if filter_by == 'all':
        product_set = Product.objects.all().order_by(sort_by)
    elif ProductCategory.objects.filter(id=filter_by).exists():
        product_set = Product.objects.filter(category=filter_by).order_by(sort_by)
    else:
        product_set = Product.objects.all().order_by(sort_by)
    if request.user.is_authenticated:
        context = {'products': product_set,
                   'today': SearchHistory.objects.filter(profile=request.user.profile, timestamp=today).order_by('-timestamp'),
                   'yesterday': SearchHistory.objects.filter(profile=request.user.profile, timestamp=yesterday).order_by('-timestamp'),
                   'lastweek': SearchHistory.objects.filter(profile=request.user.profile, timestamp__lt=yesterday, timestamp__gte=lastweek).order_by('-timestamp'),
                   'older': SearchHistory.objects.filter(profile=request.user.profile, timestamp__lt=lastweek).order_by('-timestamp'),
                   'categories': categories
                   }
    else:
        context = {'products': product_set,
                   'categories': categories
                   }
    return render(request, 'products/index.html', context)


def get_product_by_id(request, id):
    return render(request, 'products/product_details.html', {
        'product': get_object_or_404(Product, pk=id)
    })


#Create new product
@login_required
@admin_required
def create_product(request):
    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)
        if form.is_valid():
            product = form.save()
            product_image = ProductImage(image=request.POST['image'], product=product)
            product_image.save()
            return redirect('product-index')
    else:
        form = ProductCreateForm()
    return render(request, 'products/create_product.html', {
        'form': form
    })


@login_required
@admin_required
def create_category(request):
    if request.method == 'POST':
        form = ProdcutCategoryCreateForm(data=request.POST)
        if form.is_valid():
            category = form.save()
            return redirect('products_categories')
    else:
        form = ProdcutCategoryCreateForm()
    return render(request, 'products/create_category.html', {
        'form': form
    })


@login_required
@admin_required
def create_manufacturer(request):
    if request.method == 'POST':
        form = ProductManufacturerCreateForm(data=request.POST)
        if form.is_valid():
            manufacturer = form.save()
            return redirect('products_manufacturers')
    else:
        form = ProductManufacturerCreateForm()
    return render(request, 'products/create_manufacturer.html', {
        'form': form
    })


@login_required
@admin_required
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('product-index')




