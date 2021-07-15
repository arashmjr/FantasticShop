from django.db import models
from Src.Domain.Entities import Carts, Product
from Src.Domain.Entities.User import User
import datetime


class CartProducts(models.Model):
    uid = models.BigAutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Carts, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now=True)
    quantity = models.BigIntegerField(blank=False)
    order_status = models.IntegerField()

