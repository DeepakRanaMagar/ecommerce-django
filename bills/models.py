from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import Customer
from cart.models import Cart

# Create your models here.

PAYMENT_CHOICES = {
    "ESEWA" : "Esewa",
    "COD" : "Cash On Delivery",
    "KHALTI" : "Khalti",
    "BANK TRANSFER" : "Bank Transfer"
}

class Bill(models.Model):
    customer = models.ForeignKey(Customer, verbose_name=_("customer"), on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, verbose_name=_("cart"), on_delete=models.CASCADE)
    shipping_address = models.CharField(_("shipping address"), max_length=50)
    billing_address = models.CharField(_("billling address"), max_length=50)
    has_paid = models.BooleanField(_("has paid"))
    payment_method = models.CharField(_("Payment Method"),choices=PAYMENT_CHOICES, max_length=50)


    class Meta:
        verbose_name = 'Bill'
        verbose_name_plural = 'Billings'
    
    def __str__(self):
        return self.shipping_address