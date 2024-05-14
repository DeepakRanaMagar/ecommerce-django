from rest_framework import serializers
from .models import Catalog, SubCatalog, Product

class CatalogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Catalog
        fields = '__all__'


class SubCatalogSerializer(serializers.ModelSerializer):
    # Catalog = CatalogSerializer()

    class Meta:
        model = SubCatalog
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # SubCatalog = SubCatalogSerializer()

    class Meta:
        model = Product
        exclude = ['image_width', 'image_height', 'image']