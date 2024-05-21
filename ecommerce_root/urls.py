from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView, SpectacularSwaggerView
)
urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')), #docs for admin panel
    path('admin/', admin.site.urls),

    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('product_merchant/', include('product_merchant.urls')),
    path('cart/', include('cart.urls')),
    path('bill/', include('bills.urls')),

    #To create a API Docs
    path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name="schema"), name="swaggerapi")

]
