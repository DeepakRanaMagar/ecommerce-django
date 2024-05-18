from django.urls import path
from .views import CartView, CartItemsView

urlpatterns = [
    path('createcart/', CartView.as_view()),
    path('addcartitem/', CartItemsView.as_view()),
]
