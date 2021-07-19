from Src.Domain.Entities.Product import Product
from django.contrib import admin


class AddProductAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'category_id', 'name', 'desc', 'price', 'url_photo', 'quantity']


admin.site.register(Product, AddProductAdmin)
