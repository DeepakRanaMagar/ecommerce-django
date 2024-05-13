from django.db import models
from django.utils.translation import gettext as _ 


class Catalog(models.Model):
    name = models.CharField(_("name"), max_length=50)

    def __str__(self):
        return self.name

class SubCatalog(models.Model):
    Catalog = models.ForeignKey(Catalog, verbose_name=_("Catalog"), on_delete=models.CASCADE)
    name = models.CharField(_("Sub Catalog"), max_length=50)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    Category = models.ForeignKey(SubCatalog, verbose_name=_("Category"), on_delete=models.CASCADE)
    name = models.CharField(_("name"), max_length=50)
    description = models.TextField(_("description"))
    price = models.DecimalField(_("price"), max_digits=6, decimal_places=2)
    image_width = models.IntegerField(default=1080)
    image_height = models.IntegerField(default=1080)
    image = models.ImageField(_("image"), upload_to='images/products/', height_field='image_height', width_field='image_width', blank=True, null=True)

    def __str__(self):
        return self.name
