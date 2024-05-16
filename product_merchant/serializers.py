from products.models import Catalog, SubCatalog, Product
from django.db import transaction, IntegrityError
from django.http import HttpResponse

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator
from rest_framework.response import Response

'''
    Serialization of the input of admin for the Catalog
'''

existing_catalog = Catalog.objects.all()    #query to fetch existing objects of catalog
existing_catalog_list = [item.name for item in existing_catalog]    #converting into list
print(existing_catalog_list)


class CatalogSerializer(serializers.Serializer):
    name = serializers.CharField()

    def validate(self, data):   # for the validation of catalog name 
        incoming_name = data.get("name")    #input name of catalog from the front end
        if incoming_name in existing_catalog_list:  #validation condition
            raise serializers.ValidationError(
                'Catalog already exists'
            )
        return data

    @transaction.atomic
    def save(self): #saving the serialized data
        name = self.validated_data['name']
        try:
            catalog = Catalog.objects.create(
                name = name,
            )
        except Exception as e:
            raise e


'''
    serialization for the sub-catalog fields that is sent from the front end through request
'''

class SubCatalogSerializer(serializers.Serializer):
    catalog = serializers.PrimaryKeyRelatedField(queryset=Catalog.objects.all())
    name = serializers.CharField()  #name of sub-catalog that comes from the request
    
    def validate(self, data):   # for the validation of catalog name 
        incoming_name = data.get("name")    #input name of catalog from the front end
        existing_subcatalog_list = SubCatalog.objects.values_list('name', flat=True)  # Dynamic fetch
        if incoming_name in existing_subcatalog_list:
            raise serializers.ValidationError('SubCatalog already exists')
        return data

    @transaction.atomic #atomic db
    def save(self): #saving the serialized data
        catalog = self.validated_data['catalog']    #fetching the validated data from the dictionary 
        name = self.validated_data['name']
        try:
            subcatalog = SubCatalog.objects.create(
                catalog =catalog,
                name = name,
            )
        except Exception as e:
            raise e
        
'''
    serialization of the product detail that is sent through the request
'''

class ProductDetailSerializer(serializers.Serializer):
    # Input fields for the Merchant
    category = serializers.PrimaryKeyRelatedField(queryset = SubCatalog.objects.all())  #PK relation of the category field of the Product detail with the sub category
    name = serializers.CharField()  #name of the product
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2)    #price of the product
    image_width = serializers.IntegerField(required=False)
    image_height = serializers.IntegerField(required=False)
    image = serializers.ImageField(required=False)
    
    @transaction.atomic # To create the db save transaction atomic
    def save(self):
        try: 
            product = Product.objects.create(
                category = self.category,
                name = self.name,
                description = self.description,
                price = self.price,
                image_width = self.image_width,
                image_height = self.image_height,
                image = self.image
            )
        except Exception as e: 
            raise e
