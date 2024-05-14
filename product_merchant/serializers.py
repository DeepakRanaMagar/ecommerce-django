from rest_framework import serializers
from products.models import Product

'''
    Serialization of the input of the Merchant
'''

class ProductDetailSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    image_width = serializers.IntegerField(required=False)
    image_height = serializers.IntegerField(required=False)
    image = serializers.ImageField(required=False)
    