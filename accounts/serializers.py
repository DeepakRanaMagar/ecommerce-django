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
    profile_pic = serializers.ImageField(required=False)
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
                password = make_password(self.validated_data['password'])
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
    profile_pic = serializers.ImageField(required=False)
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
                password = make_password(self.validated_data['password'])
            )
            merchant = Merchant.objects.create(
                user = user,
                merchant_name = self.validated_data['merchant_name'],
                pan_no = self.validated_data['pan_no'],
                address1 = self.validated_data['address1'],
                address2 = self.validated_data['address2'],
            )
            if 'profile_pic' in self.validated_data:
                merchant.profile_pic = self.validated_data['profile_pic']
                merchant.save()

        except Exception as e:
            raise serializers.ValidationError(f"An error occurred: {e}")

'''
    Serializer for Customer Profile
'''
class CustomerSerializer(serializers.ModelSerializer):
    profile_pic = serializers.ImageField(source='customer.profile_pic', required=False)
    dob = serializers.DateField(source='customer.dob')
    address1 = serializers.CharField(source='customer.address1', required=False)
    address2 = serializers.CharField(source='customer.address2', required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'profile_pic', 'dob', 'address1', 'address2']

class MerchantSerializer(serializers.ModelSerializer):
    # profile_pic = serializers.ImageField(source='merchant.profile_pic', required=False)
    # merchant_name = serializers.CharField(source= 'merchant.merchant_name')
    # pan_no = serializers.DateField(source='merchant.pan_no')
    # address1 = serializers.CharField(source='merchant.address1', required=False)
    # address2 = serializers.CharField(source='merchant.address2', required=False)
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.EmailField(source='user.email')
    
    class Meta:
        model = Merchant
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'profile_pic', 'merchant_name','pan_no', 'address1', 'address2']