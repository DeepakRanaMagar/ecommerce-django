from rest_framework import serializers
from .models import Customer, Merchant
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib.auth.hashers import make_password

'''
    Customer Registration
'''
class CustomerRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    dob = serializers.DateField()
    address1 = serializers.CharField(required=True)
    address2 = serializers.CharField(required=False)


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
                user = user,
                dob = self.validated_data['dob'],
                address1 = self.validated_data['address1'],
                address2 = self.validated_data['address2'],
            )
        except Exception as e:
            raise e
        
'''
    Merchant Registration
'''
class MerchantRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    merchant_name = serializers.CharField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    pan_no = serializers.IntegerField()
    address1 = serializers.CharField(required=True)
    address2 = serializers.CharField(required=False)
    
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

            merchant = Merchant.objects.create(
                user = user,
                merchant_name = self.validated_data['merchant_name'],
                pan_no = self.validated_data['pan_no'],
                address1 = self.validated_data['address1'],
                address2 = self.validated_data['address2'],
            )
        except Exception as e:
            raise e