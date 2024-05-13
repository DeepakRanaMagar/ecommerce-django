from django.contrib import admin
from .models import Catalog, SubCatalog

@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(SubCatalog)
class SubCatalogAdmin(admin.ModelAdmin):
    list_display = ['Catalog','name']

    def Catalog(self, obj):
        return obj.Catalog.name