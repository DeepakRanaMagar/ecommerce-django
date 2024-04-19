from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
# from django import forms

class RegisterForm(UserCreationForm):
    class Meta():
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email']
