from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.core.validators import MaxValueValidator

class Customer(models.Model):
    profile_pic = models.ImageField(upload_to='images/customer%Y/%m/%d/', blank=True, null=True)
    user = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.CASCADE)
    dob = models.DateField(_("date of birth"), auto_now=False, auto_now_add=False)
    address1 = models.CharField(max_length=150, null=True, blank=True)
    address2 = models.CharField(max_length=150, null=True, blank=True)
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
class Merchant(models.Model):
    profile_pic = models.ImageField(upload_to='images/merchant%Y/%m/%d/', blank=True, null=True)
    user = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.CASCADE)
    merchant_name = models.CharField(_("merchant name"), max_length=50)
    pan_no = models.IntegerField(_("Pan No"), validators=[MaxValueValidator(999999999)])
    address1 = models.CharField(max_length=150, null=True, blank=True)
    address2 = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self): 
        return f"{self.merchant_name}"