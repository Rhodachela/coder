from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductSearchView,
    ProductCreateView,
    ProductUpdateView,
)
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('list/', ProductListView.as_view(), name='product-list'),  # Matches /api/products/
    path('search/', ProductSearchView.as_view(), name='product-search'),  # Matches /api/products/search/
    path('<int:id>/', ProductDetailView.as_view(), name='product-detail'),  # Matches /api/products/<id>/
    path('create/', ProductCreateView.as_view(), name='product-create'),  # Matches /api/products/create/
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),  # Matches /api/products/update/<id>/
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Token authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT refreshing
]
