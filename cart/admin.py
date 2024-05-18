from django.contrib import admin
from .models import Cart, CartItems
# Register your models here.

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['customer','created_at']

@admin.register(CartItems)
class CartItemsAdmin(admin.ModelAdmin):
    list_display = ['cart','product', 'quantity']