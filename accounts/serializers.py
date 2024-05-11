from rest_framework import serializers
from .models import Customer, Merchant
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib.auth.hashers import make_password

class CustomerRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    dob = serializers.DateField()

    def validate(self, data):
        if data.get("password") != data.get("confirm_password"):
            raise serializers.ValidationError("Incorrect Password.")
        if User.objects.filter(email=data.get("email")).exists():
            raise serializers.ValidationError("Email is already used.")
        if User.objects.filter(username=data.get("username")).exists():
            raise serializers.ValidationError("Username is already taken.")
        return data
    @transaction.atomic
    def save(self):
        try:
            user = User.objects.create(
                email = self.validated_data['email'],
                username = self.validated_data['username'],
                first_name = self.validated_data['first_name'],
                last_name = self.validated_data['last_name'],
                password = make_password(self.validated_data['email'])
            )

            customer = Customer.objects.create(
                user = user
                dob = self.validated_data['dob']
            )
        except Exception as e:
            raise e
        