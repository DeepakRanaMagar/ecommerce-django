from django.urls import path
from .views import CatalogView, SubCatalogView, ProductDetailView

urlpatterns = [
    path('update/catalog/', CatalogView.as_view()),
    path('update/subcatalog/', SubCatalogView.as_view()),
    path('update/productdetail/', ProductDetailView.as_view())
]
