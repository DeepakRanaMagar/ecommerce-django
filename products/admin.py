from django.contrib import admin
from .models import Catalog, SubCatalog

@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(SubCatalog)
class SubCatalogAdmin(admin.ModelAdmin):
    list_display = ['get_catalog','name']

    def get_catalog(self, obj):
        return self.obj.Catalog.name