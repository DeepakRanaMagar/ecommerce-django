from django.shortcuts import render
from .serializers import CustomerRegistrationSerializer, MerchantRegistrationSerializer
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status

'''
    Registration Section
'''
class CustomerRegistrationView(APIView):
    permission_classes = [AllowAny,]

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