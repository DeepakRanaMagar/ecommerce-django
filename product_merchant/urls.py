from django.urls import path
from .views import CatalogView

urlpatterns = [
    # path('', ProductDetailView.as_view())
    path('', CatalogView.as_view())
]
