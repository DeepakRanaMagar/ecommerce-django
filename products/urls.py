from django.urls import path
from .views import ProductView, CatalogView, SubCatalogView

urlpatterns = [
    path('productdetail/', ProductView.as_view()),
    path('catalog/', CatalogView.as_view()),
    path('subcatalog/', SubCatalogView.as_view()),
]
