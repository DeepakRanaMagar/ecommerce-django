from django.shortcuts import render

from .serializers import BillSerializer
from .models import Bill
from accounts.models import Customer
from cart.models import Cart

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class BillView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        user = (
            request.user
        )  # fetch the request sending user, but we need to verify whether the 'user' is customer or merchant
        # print(user)
        try:  # exception handling
            is_customer = Customer.objects.get(
                user=user
            )  # fetch the user from the Customer DB if the requested user matches
        except Customer.DoesNotExist as e:  # if the is_customer condition fails performs following code
            return Response(
                {"Error: Only Customers are allowed to create a Cart"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        request.data["customer"] = is_customer.id
        # print(request.data["customer"])
        print(request.data)
        

        '''
            login vako customer ko cart xa ki xaina tyo ni detemine garnu paryo 
            ani automatically, serialize huna paryo
        
        '''
        seriailzer = BillSerializer(data=request.data)