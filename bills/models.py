from django.db import models
from address.models import AddressField
from django.utils.translation import gettext_lazy as _
# Create your models here.

PAYMENT_CHOICES = {
    "ESEWA" : "Esewa",
    "COD" : "Cash On Delivery",
    "KHALTI" : "Khalti",
    "BANK TRANSFER" : "Bank Transfer"
}

class Bill(models.Model):
    
    shipping_address = AddressField(related_name='ship_address',null=True, blank=True)
    billing_address = AddressField(related_name='bill_address',null=True, blank=True)
    has_paid = models.BooleanField(_("has paid"))
    payment_method = models.CharField(_("Payment Method"),choices=PAYMENT_CHOICES, max_length=50)

    class Meta:
        verbose_name = 'Billing'
        verbose_name_plural = 'Billing'
    
    def __str__(self):
        return self.shipping_address