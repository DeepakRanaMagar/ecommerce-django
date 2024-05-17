from django.shortcuts import render
from .serializers import CustomerRegistrationSerializer, MerchantRegistrationSerializer, CustomerSerializer, MerchantSerializer
from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from .models import Customer, Merchant


'''
    Registration Section
'''
class CustomerRegistrationView(APIView):
    permission_classes = [AllowAny,]


    # To Create a new Customer User account
    def post(self, request):
        serializer = CustomerRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            try: 
                serializer.save()
                return JsonResponse(
                    {
                        "Success": "Customer Successfully Registered"
                    }, status = status.HTTP_201_CREATED
                )
            except Exception as e:
                return JsonResponse(
                    {
                        "error": f"Unable to register Customer {str(e)}"
                    }, status = status.HTTP_400_BAD_REQUEST
                )
        return JsonResponse(
            {
                "serializer error": serializer.error_messages
            }, status =status.HTTP_400_BAD_REQUEST
        )
    
    # To update the details in the customer accounts
    



class MerchantRegistrationView(APIView):
    permission_classes = [AllowAny,]

    def post(self, request):
        serializer = MerchantRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            try: 
                serializer.save()
                return JsonResponse(
                    {
                        "Success": "Merchant Successfully Registered"
                    }, status = status.HTTP_201_CREATED
                )
            except Exception as e:
                return JsonResponse(
                    {
                        "error": f"Unable to register Merchant {str(e)}"
                    }, status = status.HTTP_400_BAD_REQUEST
                )
        return JsonResponse(
            {
                "serializer error": serializer.error_messages
            }, status =status.HTTP_400_BAD_REQUEST
        )
    
class UserLoginView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "token": token.key,
                    "user_id": user.id
                }, status= status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "error": "Login Failed. Invalid Credentials"
                }, status=status.HTTP_401_UNAUTHORIZED
            )

class UserLogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.auth.delete()
        return Response(
            {"message": "Successfully logged out"}, status=status.HTTP_200_OK
        )
    

'''
    View to list all the Customer and Merchant users
'''

class CustomerList(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        '''
            return all the Customers with their usernames
        '''
        customers = Customer.objects.all().values('id', 'user__username')  # Use values or select_related

        customer_data = [
            {'id': customer['id'], 'username': customer['user__username']}
            for customer in customers
        ]
        return Response(customer_data)
    
    
class MerchantList(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        '''
            return all the Merchants
        '''
        merchants = Merchant.objects.all().values('user', 'user__username')  # Use values or select_related
        merchant_data = [
                    {'id': merchant['user'], 'username': merchant['user__username']}
                    for merchant in merchants
                ]
        return Response(
            merchant_data
        )
    

'''
    View to return Details of the particular Customer and Merchant
'''

class CustomerDetails(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        try:
            customer_detail = Customer.objects.get(user_id=pk)
        except Customer.DoesNotExist:
            return Response(
                {"detail": "Customer isn't registered yet"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CustomerSerializer(customer_detail.user)
        return Response(serializer.data)


class MerchantDetails(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        try:
            merchant = Merchant.objects.get(user_id=pk)
        except Exception as e:    
            return Response(
                {
                    "detail": "Merchant isn't registered yet"
                }, status= status.HTTP_404_NOT_FOUND
            )
        serializer = MerchantSerializer(merchant)
        return Response(serializer.data)
        