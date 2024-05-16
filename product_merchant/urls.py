from django.urls import path
from .views import CatalogView

urlpatterns = [
    # path('', ProductDetailView.as_view())
    path('update/catalog/', CatalogView.as_view()),
    path('update/subcatalog/', CatalogView.as_view()),

]
