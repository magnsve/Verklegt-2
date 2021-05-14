from django.urls import path
from . import views

#URLS that the cart and payment process uses
urlpatterns = [
    path('', views.index, name='cart-index'),
    path('contact', views.contact, name="contact"),
    path('add/<int:id>', views.add_to_cart, name='add-to-cart'),
    path('increase_by_one/<int:id>', views.increase_by_one, name='increase-by-one'),
    path('decrease_by_one/<int:id>', views.decrease_by_one, name='decrease-by-one'),
    path('payment', views.payment, name='payment'),
    path('review', views.review, name='review'),
    path('confirmation', views.confirmation, name='confirmation'),
]
