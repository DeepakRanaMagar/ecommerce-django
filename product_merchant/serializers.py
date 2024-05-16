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
    serialization for the sub-catalog fields that is sent from the front end
'''
existing_subcatalog = SubCatalog.objects.all()    #query to fetch existing objects of sub-catalog
existing_subcatalog_list = [item.name for item in existing_subcatalog]    #converting into list
print(existing_subcatalog_list)

class SubCatalogSerializer(serializers.Serializer):
    catalog = serializers.ChoiceField(choices=existing_catalog_list)    #cause we need to select sub-catalogs based on the parent catalogs
    name = serializers.CharField()  #name of sub-catalog that comes from the request
    
    def validate(self, data):   # for the validation of catalog name 
        incoming_name = data.get("name")    #input name of catalog from the front end
        if incoming_name in existing_subcatalog_list:  #validation condition
            raise serializers.ValidationError(
                'SubCatalog already exists'
            )
        return data

    @transaction.atomic
    def save(self): #saving the serialized data
        name = self.validated_data['name']
        try:
            subcatalog = SubCatalog.objects.create(
                name = name,
            )
        except Exception as e:
            raise e


# catalog = Catalog.objects.all()
# catalog_list = [item.name for item in catalog]
# # print(catalog_list)

# subcatalog = SubCatalog.objects.all()
# subcatalog_list = [item.name for item in subcatalog]
# print(subcatalog_list)


# class ProductDetailSerializer(serializers.Serializer):
#     # Input fields for the Merchant
#     # catalog = serializers.ChoiceField(choices=catalog_list)
#     # subcatalog = serializers.ChoiceField(choices=subcatalog_list)
    
#     # category = serializers.ChoiceField(choices=subcatalog_list)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     price = serializers.DecimalField(max_digits=6, decimal_places=2)
#     image_width = serializers.IntegerField(required=False)
#     image_height = serializers.IntegerField(required=False)
#     image = serializers.ImageField(required=False)
    
#     @transaction.atomic # To create the db save transaction atomic
#     def save(self):
#         try: 
#             product = Product.objects.create(
#                 category = self.category,
#                 name = self.name,
#                 description = self.description,
#                 price = self.price,
#                 image_width = self.image_width,
#                 image_height = self.image_height,
#                 image = self.image
#             )
#         except Exception as e: 
#             raise e
