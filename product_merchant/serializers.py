from products.models import Catalog, SubCatalog, Product
from django.db import transaction, IntegrityError
from django.http import HttpResponse

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator
from rest_framework.response import Response

'''
    Serialization of the input of the Merchant
'''
# catalog_query = Catalog.objects.all() 
# catalog_list = [item.name for item in catalog_query]
# print(catalog_list)

class CatalogSerializer(serializers.Serializer):
    name = serializers.CharField()

    def validate_name(self, value):
        if Catalog.objects.filter(name = value).exists():
            pass
        else:
            return value
    
    @transaction.atomic
    def save(self):
        name = self.validated_data['name']
        print(name)
        try:
            catalog = Catalog.objects.create(
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
