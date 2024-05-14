from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Catalog, SubCatalog, Product
from .serializers import ProductSerializer
from rest_framework.permissions import AllowAny

class ProductView(APIView):
    permission_classes = [AllowAny, ]
    
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset)
        return JsonResponse(serializer.data)

