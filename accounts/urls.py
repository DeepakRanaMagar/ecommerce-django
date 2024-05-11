from django.urls import path, include
from .views import CustomerRegistrationView
urlpatterns = [
    path('register/', CustomerRegistrationView.as_view(), name='CustomerRegistration'),
]
