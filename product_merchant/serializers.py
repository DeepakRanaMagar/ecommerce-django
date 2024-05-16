from rest_framework import serializers
from products.models import Catalog, SubCatalog, Product
from django.db import transaction

'''
    Serialization of the input of the Merchant
'''
class CatalogSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)

    @transaction.atomic
    def save(self):
        try:
            catalog = Catalog.objects.create(
                name=self.name
            )
            print(catalog)
        except Exception as e: 
            raise serializers.ValidationError('error', e)

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
