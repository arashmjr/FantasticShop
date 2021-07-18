from django.db import models
from Src.Domain.Entities import User, Carts
from django.contrib import admin


class Order(models.Model):
    order_id: models.BigAutoField(primary_key=True, blank=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Carts, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now=True)


