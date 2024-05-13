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