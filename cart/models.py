from django.db import models
from django.conf import settings
from products.models import Product
# Create your models here.
class Cart(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    quantity = models.FloatField()
    manufacturer = models.ForeignKey(ProductManufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.CharField(max_length=9999)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

#Einn klasi sem er cart
#I honum er ID
#ProfileID, eða user ID
#isOpen boolean field
#Foreignkey í bæði product
#Quanity field eins og price
#AddressID eða Address field
#Tafla fyrir items sem inniheldur cartID
