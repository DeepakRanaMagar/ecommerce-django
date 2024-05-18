from django.urls import path
from .views import CartView, CartItemsView

urlpatterns = [
    path('cart/', CartView.as_view()),
    path('cartitem/', CartItemsView.as_view()),
]
