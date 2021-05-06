from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="administrate-index"),
    path('administrate_users', views.administrate_users, name='administrate_users'),
    path('administrate_products', views.administrate_products, name='administrate_products'),
    path('toggle_admin/<int:id>', views.toggle_admin, name='toggle_admin'),
    path('administrate_products/<int:id>', views.update_product, name='update_product')
]