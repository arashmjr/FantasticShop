from Src.Domain.Entities.Carts import Carts
from Src.Domain.Entities.CartProducts import CartProducts
from django.contrib import admin


class AddToCartAdmin(admin.ModelAdmin):
    list_display = ['uid', 'product_id', 'cart_id', 'user_id', 'creation_date', 'quantity','order_status']


admin.site.register(CartProducts, AddToCartAdmin)

