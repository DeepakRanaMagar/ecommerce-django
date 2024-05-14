from rest_framework import serializers
from .models import Catalog, SubCatalog, Product

# class CatalogSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Catalog
#         fields = '__all__'


class SubCatalogSerializer(serializers.ModelSerializer):
    # Catalog = CatalogSerializer()

    class Meta:
        model = SubCatalog
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = SubCatalogSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['category','name', 'description', 'price']