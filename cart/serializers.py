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
    customer = serializers.PrimaryKeyRelatedField(queryset = Customer.objects.all())
    class Meta:
        model = Cart
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

    def create(self, validated_data):
        return CartItems.objects.create(**validated_data)

    # @transaction.atomic
    # def save(self):
    #     try:
    #         cart_items = CartItems.objects.create(
    #             cart = self.validated_data.get('cart'),
    #             product = self.validated_data.get('product'),
    #             quantity = self.validated_data.get('quantity')
    #         )
    #         print(cart_items)
        
    #     except Exception as e:
    #         return Response(
    #             {
    #                 "Exception": str(e)
    #             }, status=status.HTTP_400_BAD_REQUEST,
    #         )