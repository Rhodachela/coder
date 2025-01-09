from django.urls import path
from .views import ProductListView, ProductDetailView, ProductSearchView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ProductCreateView, ProductUpdateView



urlpatterns = [
    # List and Create Products
    path('', ProductListView.as_view(), name='product-list'),  # Matches /products/
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    # Retrieve, Update, and Delete a Product
    path('search/', ProductSearchView.as_view(), name='product-search'),  # New search endpoint
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:id>/', ProductDetailView.as_view(), name='product-detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),


]
