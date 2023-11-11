from django.contrib import admin

from .models import User
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name',"phone_number","last_name"]
    list_editable = ['phone_number']

admin.site.register(User,UserAdmin)