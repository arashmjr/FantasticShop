from Src.Domain.Entities.User import User
from django.contrib import admin


class SaveUser(admin.ModelAdmin):
    list_display = ['user_id','name', 'email','password', 'access_level',
                    'address', 'postal_code', 'phone_number']


admin.site.register(User, SaveUser)

