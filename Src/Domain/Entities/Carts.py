from django.db import models
from .Product import Product
from Src.Domain.Entities.User import User
import datetime


class Carts(models.Model):
    Cart_id = models.OneToOneField(primary_key=True, on_delete=models.CASCADE,)
    # user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    # product_id = models.BigIntegerField(blank=False)
    product_name = models.CharField(max_length=40, blank=False, null=False)
    quantity = models.IntegerField(blank=False)
    isActive = models.BooleanField(default=True)
    creation_date = models.DateTimeField(default=datetime.datetime.now)

