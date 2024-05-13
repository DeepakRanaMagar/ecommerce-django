from django.db import models
from django.utils.translation import gettext as _


class Product(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    category = models.CharField(_("category"), max_length=50)
    description = models.CharField(_("Description"), max_length=50)
    price = models.DecimalField(_("price"), max_digits=6, decimal_places=2)
    image = models.ImageField(_("image"), upload_to='media/images/products', height_field=1080, width_field=1080, max_length=None)

    def __str__(self):
        return self.name