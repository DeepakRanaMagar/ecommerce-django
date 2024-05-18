from django.db import transaction

from .models import Cart, CartItems
from accounts.models import Customer
from accounts.serializers import CustomerSerializer

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

class CartSerializer(serializers.Serializer):
    customer = CustomerSerializer(many=False)
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