from rest_framework import serializers
from .models import Bill
from accounts.models import Customer
from cart.models import Cart

class BillSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(
        queryset = Customer.objects.all()
    )
    cart = serializers.PrimaryKeyRelatedField(
        queryset = Cart.objects.all()
    )
    class Meta:
        model = Bill
        fields = '__all__'
    
    def create(self, validated_data):
        return Bill.objects.create(**validated_data)
        