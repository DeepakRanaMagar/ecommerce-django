from django.urls import path
from .views import BillView

urlpatterns = [
    path('', BillView.as_view())
]
