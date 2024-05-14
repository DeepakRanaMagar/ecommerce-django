from django.contrib import admin
from .models import Catalog, SubCatalog, Product

@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    
@admin.register(SubCatalog)
class SubCatalogAdmin(admin.ModelAdmin):
    list_display = ['get_catalog_name','name']
    # search_fields = ['Catalog','name']
    
    def get_catalog_name(self, obj):
        return obj.Catalog.name
    get_catalog_name.short_decription = 'Catalog'
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    search_fields = ["name", "price"]

    # def Category(self, obj):
    #     return obj.SubCatalog
    
