from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="administrate-index"),
    path('users', views.administrate_users, name='administrate_users'),
    path('products', views.administrate_products, name='administrate_products'),
    path('toggle_admin/<int:id>', views.toggle_admin, name='toggle_admin'),
    path('products/products', views.product_products, name='products_products'),
    path('products/products/<int:id>', views.update_product, name="update_product"),
    path('products/delete_product/<int:id>', views.delete_product, name='delete_product'),
    path('products/create_product', views.create_product, name='create_product'),
    path('products/manufacturers', views.administrate_manufacturers, name='products_manufacturers'),
    path('manufacturers/<int:id>', views.update_manufacturer, name='update_manufacturer'),
    path('delete_manufacturers/<int:id>', views.delete_manufacturer, name='delete_manufacturer'),
    path('products/categories', views.administrate_categories, name='products_categories'),
    path('categories/<int:id>', views.update_category, name='update_category'),
    path('delete_category/<int:id>', views.delete_category, name='delete_category')
]