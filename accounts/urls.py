from django.urls import path, include
from .views import CustomerRegistrationView, MerchantRegistrationView, UserLoginView, UserLogoutView

urlpatterns = [
    path('register/customer/', CustomerRegistrationView.as_view(), name='CustomerRegistration'),
    path('register/merchant/', MerchantRegistrationView.as_view(), name='MerchantRegistration'),
    path('login/', UserLoginView.as_view(), name='UserLogin'),
    path('logout/', UserLogoutView.as_view(), name='UserLogin'),
]
