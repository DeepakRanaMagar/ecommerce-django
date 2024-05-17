from django.shortcuts import render
from .models import Cart, CartItems
from .serializers import CartSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        pass