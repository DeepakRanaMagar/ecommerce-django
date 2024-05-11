from django.contrib import admin
from .models import Customer, Merchant

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['dob']

'''
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['get_full_name', 'dob']  # Add 'get_full_name' to display first name and last name

    def get_full_name(self, obj):
        return obj.user.get_full_name()  # Accessing the user's full name
    get_full_name.short_description = 'Full Name'  # Customizing the column name in the admin panel

'''
@admin.register(Merchant)
class MerchantAdmin(admin.ModelAdmin):
    list_display = ['merchant_name']