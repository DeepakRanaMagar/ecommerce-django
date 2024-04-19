from django.urls import path, include
from .views import sign_up

urlpatterns = [
    path('register/', sign_up, name='user_registration'),
]
