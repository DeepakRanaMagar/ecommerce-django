from django.contrib import admin
from .models import Catalog, SubCatalog, Product

@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    
@admin.register(SubCatalog)
class SubCatalogAdmin(admin.ModelAdmin):
    list_display = ['Catalog','name']
    search_fields = ['Catalog','name']
    def Catalog(self, obj):
        return obj.Catalog.name
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["Category","name", "price"]
    search_fields = ["Category","name", "price"]

    def Category(self, obj):
        return obj.SubCatalog.name
    
