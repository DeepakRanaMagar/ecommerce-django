from django.shortcuts import render
from rest_framework.views import APIView
from .models import Catalog, SubCatalog, Product
from .serializers import ProductSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
class ProductView(APIView):
    permission_classes = [AllowAny, ]
    
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

