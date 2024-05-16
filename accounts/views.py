from django.shortcuts import render
from .serializers import CustomerRegistrationSerializer, MerchantRegistrationSerializer
from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token


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