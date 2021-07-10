from Src.Domain.Entities.ShoppingCart import ShoppingCart
from django.contrib import admin


class AddToShoppingCartAdmin(admin.ModelAdmin):
    list_display = ['shoppingCart_id', 'user_id','product_id', 'product_name', 'quantity',
                    'isActive', 'creation_date']


admin.site.register(ShoppingCart, AddToShoppingCartAdmin)
