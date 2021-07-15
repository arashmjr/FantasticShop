from django.db import models
from django.contrib import admin


class Product(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    category_id = models.BigIntegerField(blank=False)
    name = models.CharField(max_length=40, blank=False, null=False)
    thumbnail = models.CharField(max_length=50, blank=False)
    price = models.BigIntegerField(blank=False)
    url_photo = models.CharField(blank=False, max_length=100)
    quantity = models.BigIntegerField(blank=False)








