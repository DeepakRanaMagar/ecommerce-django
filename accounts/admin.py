from django.contrib import admin
from django.contrib.auth.models import User
from .models import Customer, Merchant

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['get_full_name','username','dob']
    
    def get_full_name(self, obj):
        return obj.user.get_full_name()
    
    def username(self, obj):
        return obj.user.username


@admin.register(Merchant)
class MerchantAdmin(admin.ModelAdmin):
    list_display = ['merchant_name']