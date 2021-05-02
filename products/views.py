from django.shortcuts import render, get_object_or_404
from products.models import Product


def index(request):
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'products/index.html', context)

def get_product_by_id(request, id):
    return render(request, 'products/product_details.html', {
        'product': get_object_or_404(Product, pk=id)
    })