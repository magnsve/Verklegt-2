from django.db import models

from products.models import Product
from user.models import Profile

#Main Cart class
class Cart(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    is_open = models.BooleanField(default=True)

#For all items in cart
class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255, blank=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=0)


class Country(models.Model):
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.country

#For payment information step in cart
class CartAddress(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    postal_code = models.CharField(max_length=255)

#Information about payment for cart
class CartPayment(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    cardholder_name = models.CharField(max_length=255)
    card_number = models.DecimalField(max_digits=16, decimal_places=0)
    expiration_date = models.DecimalField(max_digits=4, decimal_places=0)
    cvc = models.DecimalField(max_digits=3, decimal_places=0)
