from Src.Domain.Entities.Carts import Carts
from django.contrib import admin


class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_id', 'user_id', 'order_status', 'creation_date']


admin.site.register(Carts, CartAdmin)
