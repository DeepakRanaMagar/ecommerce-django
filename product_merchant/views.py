from django.shortcuts import render
from .serializers import CatalogSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from accounts.models import Merchant



class CatalogView(APIView):
    permission_classes = [IsAdminUser, ]

    def post(self, request):
        admin = request.user.username
        print(request.data)
        serializer = CatalogSerializer(data=request.data)
        if serializer.is_valid():
            try: 
                serializer.save()
                return Response("Sucessfully Updated the Catalog with {}".format(request.data))
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