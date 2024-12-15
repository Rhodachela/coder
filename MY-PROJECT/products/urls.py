from django.urls import path
from .views import ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('api/products/', ProductListView.as_view(), name='product-list'),
    
]