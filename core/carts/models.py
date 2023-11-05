from uuid import uuid4
from django.db import models
from products.models import Product
# Create your models here.

class carts(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    create_at = models.DateField(auto_now_add=True)


class cartsItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    carts = models.ForeignKey(carts,on_delete=models.CASCADE,related_name="items")
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,related_name="product",null=True,blank=True)
    quntity = models.SmallIntegerField(null=True,blank=True)

    class Meta:
        unique_together = ("carts", "product")
