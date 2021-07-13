from Src.Domain.Entities.Carts import Carts
from django.contrib import admin


class AddToCartAdmin(admin.ModelAdmin):
    list_display = ['shoppingCart_id', 'user_id','product_id', 'product_name', 'quantity',
                    'isActive', 'creation_date']


admin.site.register(Carts, AddToCartAdmin)

