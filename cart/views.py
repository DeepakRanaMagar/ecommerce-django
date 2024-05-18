from django.shortcuts import render
from .models import Cart, CartItems
from .serializers import CartSerializer, CartItemSerializer
from accounts.models import Customer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = (
            request.user
        )  # fetch the request sending user, but we need to verify whether the 'user' is customer or merchant
        # print(customer)
        """
            other concept: Passing <int: pk> to represent the user id but will only represent 'id' of default Django Auth Model
        """
        try:  # exception handling
            is_customer = Customer.objects.get(
                user=user
            )  # fetch the user from the Customer DB if the requested user matches
            # print(is_customer.id)s
        except (
            Customer.DoesNotExist
        ) as e:  # if the is_customer condition fails performs following code
            return Response(
                {"Error: Only Customers are allowed to create a Cart"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        request.data["customer"] = is_customer.id
        serializer = CartSerializer(
            data=request.data
        )  # passes the request.data into the serializer i.e CartSerializer
        if serializer.is_valid():  # checks the validity
            try:
                serializer.save()  # saves the serialized data
                return Response(
                    {f"{request.user.first_name}, Your Cart is successfully created."},
                    status=status.HTTP_201_CREATED,
                )
            except Exception as e:
                return Response(str(e))
        return Response(
            {
                "Unable to create the Cart"
            }, status=status.HTTP_403_FORBIDDEN
        )
class CartItemsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = (
            request.user
        )  # fetch the request sending user, but we need to verify whether the 'user' is customer or merchant
        # print(customer)
        """
            other concept: Passing <int: pk> to represent the user id but will only represent 'id' of default Django Auth Model
        """
        try:  # exception handling
            is_customer = Customer.objects.get(
                user=user
            )  # fetch the user from the Customer DB if the requested user matches
            # print(is_customer.id)s
        except (
            Customer.DoesNotExist
        ) as e:  # if the is_customer condition fails performs following code
            return Response(
                {"Error: Only Customers are allowed to create a Cart"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        # request.data["customer"] = is_customer.id
        cart, created = Cart.objects.get_or_create(customer=is_customer)
        request.data["cart"] = cart.id
        # print(request.data)
        serializer = CartItemSerializer(data=request.data)  # passes the request.data into the serializer i.e CartSerializer
        print(serializer)
        if serializer.is_valid():  # checks the validity
            try:
                serializer.save()  # saves the serialized data
                
                return Response(
                    {
                        f"{request.user.username}, Your Items are successfully added to the Cart."
                    },
                    status=status.HTTP_201_CREATED,
                )
            except Exception as e:
                return Response(str(e))
        
        return Response(
            {
                "something went wrong"
            }, status=status.HTTP_403_FORBIDDEN
        )

# class CartItemsView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         user = request.user  # fetching the unverified request user
        
#         try:
            
#             customer = Customer.objects.get(
#                 user=user
#             )  # verifying the category of the requesting user
#             return Response({"you are a customer"})
        
#         except Customer.DoesNotExist as e:

#             return Response(
#                 {
#                     "Error: Only Customers are allowed to add items their Cart"
#                 },
#                 status=status.HTTP_401_UNAUTHORIZED,
#             )
        
#         serializer = CartItemSerializer(data=request.data)

#         if serializer.is_valid():
#             try:
#                 serializer.save()
#                 return Response(
#                     {f"{request.user.username}, Items is successfully added to your Cart."},
#                     status=status.HTTP_201_CREATED,
#                 )
#             except Exception as e:
#                 raise e

#         return Response(
#             {"Error: Only Customers are allowed to added Cart Items"},
#             status=status.HTTP_401_UNAUTHORIZED,
#         )
