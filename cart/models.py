from django.db import models
from products.models import Product
from user.models import Profile


class Cart(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    is_open = models.BooleanField(default=True)


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField()
    total_price = models.FloatField()


class Country(models.Model):
    country = models.CharField(max_length=255)


class CartAddress(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    postal_code = models.CharField(max_length=255)


class CartPayment(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    cardholder_name = models.CharField(max_length=255)
    card_number = models.FloatField()
    expiration_date = models.FloatField()
    cvc = models.FloatField()
