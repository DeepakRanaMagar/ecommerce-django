from rest_framework import serializers
from .models import Product
from django.db import transaction

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    category = serializers.CharField()
    description = serializers.CharField(required=False)
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    image = serializers.ImageField()

    @transaction.atomic
    def save(self):
        try:
            product = Product.objects.create(
                name = self.name,
                category = self.category,
                description = self.description,
                price = self.price,
                image = self.image
            )
        except Exception as e: 
            raise e