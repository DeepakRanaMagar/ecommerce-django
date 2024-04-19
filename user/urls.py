from django.urls import path, include
from .views import register


urlpatterns = [
    path('account/register/', register, name="Register Page")
]
