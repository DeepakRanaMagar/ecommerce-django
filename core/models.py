from django.db import models
from django.utils.translation import gettext as _


class Product(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    category = models.CharField(_("category"), max_length=50)
    description = models.CharField(_("Description"), max_length=50)
    price = models.DecimalField(_("price"), max_digits=6, decimal_places=2)
    image_width = models.IntegerField(default=1080)
    image_height = models.IntegerField(default=1080)
    image = models.ImageField(_("image"), upload_to='images/products/', height_field='image_height', width_field='image_width', blank=True, null=True)

    def __str__(self):
        return self.name