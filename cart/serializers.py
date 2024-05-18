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

class CartItemSerializer(serializers.Serializer):
    cart = CartSerializer(read_only=True)
    # product = ProductSerializer(many=True, read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset = Product.objects.all())
    quantity = serializers.IntegerField(validators=[MinValueValidator(1)])

    @transaction.atomic
    def save(self):
        try:
            cart_items = CartItems.objects.create(
                cart = self.validated_data['cart'],
                product = self.validated_data['product'],
                quantity = self.validated_data['quantity']
            )
        except Exception as e:
            return Response(
                {
                    "Exception": str(e)
                }, status=status.HTTP_400_BAD_REQUEST
            )