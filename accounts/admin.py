from django.contrib import admin
# from django.contrib.auth.models import User
from .models import Customer, Merchant

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['get_id','name','username','email','dob']
    search_fields = ['name','username','email','dob']
    
    def name(self, obj):
        return obj.user.get_full_name()
    
    def username(self, obj):
        return obj.user.username
    
    def email(self, obj):
        return obj.user.email
    
    def get_id(self, obj):
        return obj.user.id


@admin.register(Merchant)
class MerchantAdmin(admin.ModelAdmin):
    list_display = ['get_id','merchant_name', 'pan_no', 'name', 'username', 'email']
    search_fields = ['merchant_name', 'pan_no', 'name', 'username', 'email']

    def name(self, obj):
        return obj.user.get_full_name()
    
    def username(self, obj):
        return obj.user.username
    
    def email(self, obj):
        return obj.user.email
    
    def get_id(self, obj):
        return obj.user.id
