from django.db import models
from django.contrib import admin


class Product(models.Model):
    product_id = models.BigIntegerField(blank=False)
    category_id = models.BigIntegerField(blank=False)
    name = models.CharField(max_length=40, blank=False, null=False)
    thumbnail = models.CharField(max_length=50, blank=False)
    price = models.BigIntegerField(blank=False)
    quantity = models.IntegerField(blank=False)





