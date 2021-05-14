from django.urls import path
from . import views

#all URLS used by product
urlpatterns = [
    path('', views.index, name="product-index"),
    path('<int:id>', views.get_product_by_id, name="product_details"),
    path('create_product', views.create_product, name='create_product'),
    path('create_category', views.create_category, name='create_category'),
    path('create_manufacturer', views.create_manufacturer, name='create_manufacturer'),
]
