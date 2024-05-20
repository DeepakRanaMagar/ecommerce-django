from django.db import transaction
from django.core.validators import MinValueValidator

from .models import Cart, CartItems

from accounts.models import Customer

from products.serializers import ProductSerializer
from products.models import Product

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

'''
    Serializer which creates the Cart of the requested Customer
'''
class CartSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset = Customer.objects.all()) #Primary Key relation with all the objects present in the Customer DB
    class Meta:
        model = Cart #CART DB
        fields = ['customer', 'created_at']

    @transaction.atomic
    def save(self):
        customer = self.validated_data.get('customer') #fetch the field "customer" from the request
        created_at = self.validated_data.get('created_at')
        try:
            cart = Cart.objects.create(
                customer = customer,
                created_at = created_at
            )        
        except Exception as e:
            raise e

class CartItemSerializer(serializers.ModelSerializer):
    cart = serializers.PrimaryKeyRelatedField(queryset=Cart.objects.all(), required=False)
    product = serializers.PrimaryKeyRelatedField(queryset = Product.objects.all())
    quantity = serializers.IntegerField(validators=[MinValueValidator(1)])

    class Meta:
        model = CartItems
        fields = ['cart', 'product', 'quantity']

    def create(self, validated_data): #create() method
        return CartItems.objects.create(**validated_data)
