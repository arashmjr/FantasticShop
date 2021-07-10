from django.db import models
import datetime

class ShoppingCart(models.Model):
    shoppingCart_id = models.BigIntegerField(blank=False)
    user_id = models.BigIntegerField(blank=False)
    product_id = models.BigIntegerField(blank=False)
    product_name = models.CharField(max_length=40, blank=False, null=False)
    quantity = models.IntegerField(blank=False)
    isActive = models.BooleanField(default=True)
    creation_date = models.DateTimeField(default=datetime.datetime.now)

