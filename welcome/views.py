from django.shortcuts import render
from products.models import ProductCategory, Product


def index(request):
    categories = ProductCategory.objects.all().order_by('name')
    filter_by = request.GET.get('category', 'all')
    if filter_by == 'all':
        product_set = Product.objects.all().order_by('name')
    elif ProductCategory.objects.filter(id=filter_by).exists():
        product_set = Product.objects.filter(category=filter_by).order_by('name')
    else:
        product_set = Product.objects.all().order_by('name')
    context = {'products': product_set,
               'categories': categories
               }
    return render(request, 'welcome/index.html', context)
