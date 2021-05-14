from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='cart-index'),
    path('contact', views.contact, name="contact"),
    path('add/<int:id>', views.add_to_cart, name='add-to-cart'),
    path('increase_by_one/<int:id>', views.increase_by_one, name='increase-by-one'),
    path('decrease_by_one/<int:id>', views.decrease_by_one, name='decrease-by-one'),
]
