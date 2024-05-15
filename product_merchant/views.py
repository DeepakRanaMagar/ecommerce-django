from django.shortcuts import render
from .serializers import ProductDetailSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from accounts.models import Merchant


class ProductDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        merchant_id = request.user.id

        # if merchant_id != 


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