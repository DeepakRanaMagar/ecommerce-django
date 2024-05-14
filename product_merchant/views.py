from django.shortcuts import render
from .serializers import ProductDetailSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class ProductDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        pass