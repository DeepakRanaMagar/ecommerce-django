from rest_framework import serializers
from .models import Catalog, SubCatalog, Product


'''
    Model Serializer section to serialize the data which is fetch from the database
'''
class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = '__all__'


class SubCatalogSerializer(serializers.ModelSerializer):
    catalog = CatalogSerializer(read_only=True)
    class Meta:
        model = SubCatalog
        fields = ['id', 'name', 'catalog']


class ProductSerializer(serializers.ModelSerializer):
    category = SubCatalogSerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['id','category','name', 'description', 'price']

