from django.urls import path, include
from .views import CustomerRegistrationView, MerchantRegistrationView

urlpatterns = [
    path('register/customer/', CustomerRegistrationView.as_view(), name='CustomerRegistration'),
    path('register/merchant/', MerchantRegistrationView.as_view(), name='MerchantRegistration'),
]
