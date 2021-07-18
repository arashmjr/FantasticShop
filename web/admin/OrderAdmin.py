from Src.Domain.Entities import Order
from django.contrib import admin


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'cart_id', 'creation_date']


admin.site.register(Order, OrderAdmin)


