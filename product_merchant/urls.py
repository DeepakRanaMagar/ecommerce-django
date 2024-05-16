from django.urls import path
from .views import CatalogView, SubCatalogView

urlpatterns = [
    # path('', ProductDetailView.as_view())
    path('update/catalog/', CatalogView.as_view()),
    path('update/subcatalog/', SubCatalogView.as_view()),

]
