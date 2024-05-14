from django.contrib import admin
from .models import Catalog, SubCatalog, Product

@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    
@admin.register(SubCatalog)
class SubCatalogAdmin(admin.ModelAdmin):
    list_display = ['catalog','name']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["category","name", "price"]
    search_fields = ["name", "price"]

