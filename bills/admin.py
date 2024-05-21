from django.contrib import admin
from .models import Bill

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['customer', 'cart','shipping_address', 'billing_address', 'has_paid', 'payment_method']
    search_display = ['customer', 'cart','shipping_address', 'billing_address', 'has_paid']
