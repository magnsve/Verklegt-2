from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="product-index"),
    path('<int:id>', views.get_product_by_id, name="product_details"),
    path('create_product', views.create_product, name='create_product'),
    path('create_category', views.create_category, name='create_category'),
    path('create_manufacturer', views.create_manufacturer, name='create_manufacturer'),
    path('delete_product/<int:id>', views.delete_product, name='delete_product'),
    path('update_product/<int:id>', views.update_product, name='update_product')
]
