from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="administrate-index"),
    path('administrate_users/<int:id>', views.administrate_users, name='administrate_users'),
    path('administrate_products', views.administrate_products, name='administrate_products'),
    path('update_user/<int:id>', views.update_profile, name='update_profile')
]
