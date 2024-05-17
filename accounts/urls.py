from django.urls import path, include
from .views import CustomerRegistrationView, MerchantRegistrationView, UserLoginView, UserLogoutView,CustomerList, MerchantList, CustomerDetails

urlpatterns = [
    path('register/customer/', CustomerRegistrationView.as_view(), name='CustomerRegistration'),
    path('register/merchant/', MerchantRegistrationView.as_view(), name='MerchantRegistration'),
    path('login/', UserLoginView.as_view(), name='UserLogin'),
    path('logout/', UserLogoutView.as_view(), name='UserLogin'),
    path('customers/', CustomerList.as_view(), name='CustomerList'),
    path('merchants/', MerchantList.as_view(), name='MerchantList'),
    path('customers/<int:pk>/', CustomerDetails.as_view(), name='CustomerDetails')
]
