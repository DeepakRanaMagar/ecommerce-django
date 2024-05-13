from django.shortcuts import render
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
# def index(request):
#     return render(request, 'landingpage.html')

class ProductView():
    permission_classes = ['IsAuthenticated',]

    def post(self, request):
        merchant = request.user
        