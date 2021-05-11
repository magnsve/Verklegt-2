from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="cart-index"),
    path('contact', views.contact, name="contact"),
    path('add/<int:id>', views.add_to_cart, name='add-to-cart')
]