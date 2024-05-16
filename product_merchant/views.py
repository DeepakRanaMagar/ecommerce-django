from django.shortcuts import render
from accounts.models import Merchant
from .serializers import CatalogSerializer, SubCatalogSerializer
from django.db import IntegrityError

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework import status


'''
    View that handles the Catalog POST request only for ADMIN 
'''

class CatalogView(APIView):
    permission_classes = [IsAdminUser, ] #allows only the admin to insert or update Catalogs

    def post(self, request):
        serializer = CatalogSerializer(data=request.data) #request.data is the data from the front end
        
        if serializer.is_valid():  # to check the validity of serialized data
            try:
                serializer.save()  # saves the serialized data
                return Response("Successfully updated the Sub Catalog", status=status.HTTP_201_CREATED)
            
            except IntegrityError: #Validation for the Catalog fields
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
            except Exception as e:
                return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SubCatalogView(APIView):
    permission_classes = [IsAdminUser, ]    #allows only the admin to insert or update Catalogs

    def post(self, request):
        serializer = SubCatalogSerializer(data=request.data)    #request.data is the data from the front end
        
        if serializer.is_valid():   # to check the validity of serialized data
            try:
                serializer.save()  # saves the serialized data
                return Response("Successfully Updated the Catalog", status=status.HTTP_201_CREATED)
            
            except IntegrityError: #Validation for the Catalog fields
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
            except Exception as e:
                return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        merchant_username = request.user.username
        # return Response(merchant_username)
        






# '''
#             def post(self, request):
#     merchant_id = request.user.id
    
#     # Assuming you have a Merchant model with a user field
#     merchant = Merchant.objects.filter(user=request.user).first()
    
#     if merchant:
#         merchant_id = merchant.id
        
#         if merchant_id != request.user.id:
#             # Handle the case where the merchant ID is different from the requested user ID
#             return Response({'error': 'Unauthorized access'}, status=status.HTTP_403_FORBIDDEN)
        
#         # Rest of your view logic
        
#         # ...
#     else:
#         return Response({'error': 'Merchant not found'}, status=status.HTTP_404_NOT_FOUND)

# '''