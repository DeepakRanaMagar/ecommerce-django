from django.db import transaction
from django.core.validators import MinValueValidator

from .models import Cart, CartItems
from accounts.models import Customer
from accounts.serializers import CustomerSerializer
from products.serializers import ProductSerializer

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

class CartSerializer(serializers.Serializer):
    customer = CustomerSerializer(many=False, read_only=True)
    created_at = serializers.DateField()

    @transaction.atomic
    def save(self):
        try:
            cart = Cart.objects.create(
                customer= self.validated_data['customer'],
                created_at = self.validated_data['created_at']
            )
        except Exception as e:
            return Response(
                {
                    "Error": str(e),
                }, status=status.HTTP_400_BAD_REQUEST
            )
class CartItemSerializer(serializers.Serializer):
    cart = CartSerializer(read_only=True)
    product = ProductSerializer(many=True, read_only=True)
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