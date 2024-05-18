from django.urls import path
from .views import CartView, CartItemsView

urlpatterns = [
    path('create/', CartView.as_view()),
    path('additems/', CartItemsView.as_view()),
]
