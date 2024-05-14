from django.shortcuts import render
from rest_framework.views import APIView
from .models import Catalog, SubCatalog, Product
from .serializers import ProductSerializer, CatalogSerializer, SubCatalogSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

'''
    Product detail view
'''
class ProductView(APIView):
    permission_classes = [AllowAny, ]
    
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
'''
    number of catalog view
'''
class CatalogView(APIView):
    permission_classes = [AllowAny, ]
    
    def get(self, request):
        queryset = Catalog.objects.all()
        serializer = CatalogSerializer(queryset, many=True)
        return Response(serializer.data)
'''
    number of sub catalog view
'''
class SubCatalogView(APIView):
    permission_classes = [AllowAny, ]
    
    def get(self, request):
        queryset = SubCatalog.objects.all()
        serializer = SubCatalogSerializer(queryset, many=True)
        return Response(serializer.data)
