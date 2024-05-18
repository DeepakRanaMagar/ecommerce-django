from django.shortcuts import render
from .models import Cart, CartItems
from .serializers import CartSerializer, CartItemSerializer
from accounts.models import Customer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        customer = request.user
        # print(customer)
        is_customer = Customer.objects.get(user=customer)
        if is_customer:
            request.data['customer'] = is_customer.id
            serializer = CartSerializer(data=request.data)
            print(serializer)
            if serializer.is_valid():
                try:
                    serializer.save()
                    return Response(
                        {
                            f"{request.user.username}, Your Cart is successfully created."
                        }, status=status.HTTP_201_CREATED
                    )
                except Exception as e:
                    raise e
        return Response(
            {
                "Error: Only Customers are allowed to create cart"
            }, status=status.HTTP_401_UNAUTHORIZED
        )
    
class CartItemsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        customer_id = request.user.id
        is_customer = Customer.objects.filter(user_id=customer_id)
        if is_customer:
            serializer = CartItemSerializer(data=request.data)

            if serializer.is_valid():
                try:
                    serializer.save()
                    return Response(
                        {
                            "{request.user.username}, Items is successfully added to your Cart."
                        }, status=status.HTTP_201_CREATED
                    )
                except Exception as e:
                    raise e
        return Response(
            {
                "Error: Only Customers are allowed to added Cart Items"
            }, status=status.HTTP_401_UNAUTHORIZED
        )