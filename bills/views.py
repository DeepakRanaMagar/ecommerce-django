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
        )   # fetch the request sending user, but we need to verify whether the 'user' is customer or merchant
        
        try:    # exception handling
            is_customer = Customer.objects.get(
                user=user
            )  # fetch the user from the Customer DB if the requested user matches
        except Customer.DoesNotExist as e:  # if the is_customer condition fails performs following code
            return Response(
                {"Error: Only customers are allowed to Bill the orders.1"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        
        print(is_customer)
        request.data["customer"] = is_customer.id  #overriding the request's "Customer field" with customer_id of the "Customer" table, because we verified the user is a customer of over system
        '''
            Fetching the cart related to Authenticated Customer, to avoid manual insertion of the cart details
        '''
        try:
            cart = Cart.objects.get(
                customer= is_customer
            )
        except Cart.DoesNotExist as e:
            return Response(
                {
                    "Error: There is not cart for this user."
                }, status=status.HTTP_400_BAD_REQUEST
            )
        
        # print("cart id", cart.id)
        request.data["cart"] = cart.id  #for automation insertion of the related cart
        
        #serialization  
        seriailzer = BillSerializer(data=request.data) #passing the data for serialization

        if seriailzer.is_valid():
            try:
                seriailzer.save()
                return Response(
                    {
                        f"{request.user.username}, Your Billing Receipt has been created. Thank you"
                    }, status=status.HTTP_201_CREATED
                )
            except Exception as e:
                return Response(str(e))
            
        return Response(
            {
                "Error: Serializer's Validation Failed"
            }, status=status.HTTP_400_BAD_REQUEST
        )