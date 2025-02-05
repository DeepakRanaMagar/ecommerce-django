from django.db import models
from django.utils.translation import gettext as _

"""
    Catalog Model
"""


class Catalog(models.Model):
    name = models.CharField(_("name"), max_length=50)  # name of the catalog

    def __str__(self):
        return self.name


"""
    Sub - Catalog Model
"""


class SubCatalog(models.Model):
    catalog = models.ForeignKey(
        Catalog, on_delete=models.CASCADE
    )  # forigen key relation to he catalog (parent)
    name = models.CharField(_("sub catalog"), max_length=50)  # name of the subcatalog

    def __str__(self):
        return self.name
        # return f"Catalog name: {self.name}"


"""
    Product Model
"""


class Product(models.Model):
    category = models.ForeignKey(
        SubCatalog, on_delete=models.CASCADE
    )  # forigen key relation to he Subcatalog
    name = models.CharField(_("name"), max_length=50)
    description = models.TextField(_("description"))
    price = models.DecimalField(_("price"), max_digits=6, decimal_places=2)
    image_width = models.IntegerField(default=1080, blank=True, null=True)
    image_height = models.IntegerField(default=1080, blank=True, null=True)
    image = models.ImageField(
        _("image"),
        upload_to="images/products/",
        height_field="image_height",
        width_field="image_width",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
