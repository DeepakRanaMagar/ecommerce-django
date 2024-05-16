from django.shortcuts import render
from .serializers import CatalogSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from accounts.models import Merchant



class CatalogView(APIView):
    permission_classes = [IsAdminUser, ] #allows only the admin to insert or update Catalogs

    def post(self, request):
        serializer = CatalogSerializer(data=request.data) #request.data is the data from the front end
        if serializer.is_valid(): #to check the validity of serialized data
            try: 
                serializer.save() #saves the serialized data 
                return Response("Sucessfully Updated the Catalog")
            except Exception as e:
                raise e 














# class ProductDetailView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         merchant_id = request.user.id
#         pass
#         # if merchant_id != 










'''
            def post(self, request):
    merchant_id = request.user.id
    
    # Assuming you have a Merchant model with a user field
    merchant = Merchant.objects.filter(user=request.user).first()
    
    if merchant:
        merchant_id = merchant.id
        
        if merchant_id != request.user.id:
            # Handle the case where the merchant ID is different from the requested user ID
            return Response({'error': 'Unauthorized access'}, status=status.HTTP_403_FORBIDDEN)
        
        # Rest of your view logic
        
        # ...
    else:
        return Response({'error': 'Merchant not found'}, status=status.HTTP_404_NOT_FOUND)

'''