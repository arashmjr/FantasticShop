from django.db import models
from django.contrib import admin


class User(models.Model):
    user_id = models.BigAutoField(blank=False, primary_key=True)
    name = models.CharField(max_length=40, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False)
    password = models.CharField(max_length=50, blank=False)
    access_level = models.IntegerField(blank=False)
    address = models.TextField()
    postal_code = models.BigIntegerField(blank=False)
    phone_number = models.BigIntegerField(blank=False)




