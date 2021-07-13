from django.db import models
from django.contrib import admin
from .Carts import Carts


class User(models.Model):
    user_id = models.BigAutoField(blank=False, primary_key=True)
    Cart_id: models.OneToOneField(Carts, unique=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False)
    password = models.CharField(max_length=50, blank=False)
    access_level = models.IntegerField(blank=False)
    address = models.TextField()
    postal_code = models.BigIntegerField(blank=False)
    phone_number = models.BigIntegerField(blank=False)





# class UserDomainModelAdmin(admin.ModelAdmin):
#     list_display = ['name', 'birth_date', 'gender']
#
#
# admin.site.register(UserDomainModel, UserDomainModelAdmin)



