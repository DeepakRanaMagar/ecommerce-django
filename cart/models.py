from django.db import models
from accounts.models import Customer, Merchant
from products.models import Product


class Cart(models.Model):
    customer = models.OneToOneField(Customer, verbose_name='customer', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True, verbose_name='created_at' )

    def __str__(self):
        return f"Cart of {self.customer.user.username}"

class CartItems(models.Model):
    cart = models.ForeignKey(Cart, verbose_name='cart', on_delete=models.CASCADE)    #relation with CART table as CartItems belongs to a table
    product = models.ForeignKey(Product, verbose_name='product', on_delete=models.CASCADE) #relation with the PRODUCT table of products app
    quantity = models.PositiveIntegerField(default=1, verbose_name='quantity')

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"