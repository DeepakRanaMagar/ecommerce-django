from django.contrib import admin
from .models import Cart, CartItems
# Register your models here.

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id','customer','created_at']
    search_fields = ['customer']

@admin.register(CartItems)
class CartItemsAdmin(admin.ModelAdmin):
    list_display = ['id','cart','product', 'quantity']
    search_display = ['cart','product', 'quantity']
