from django.urls import path
from .views import ProductDetailView

urlpatterns = [
    path('', ProductDetailView.as_view())
]
