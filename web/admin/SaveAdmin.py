from Src.Domain.Entities.UserAdmin import UserAdmin
from django.contrib import admin


class SaveAdmin(admin.ModelAdmin):
    list_display = ['admin_id', 'name', 'email', 'password', 'creation_date']


admin.site.register(UserAdmin, SaveAdmin)