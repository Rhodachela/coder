from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .models import Product
from .serializers import ProductSerializer, ProductWriteSerializer
from django.db.models import Q
from .pagination import ProductPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication  # For JWT Authentication
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .permissions import IsAdminUser


class ProductListView(generics.ListCreateAPIView):
    """
    Handles listing and creating products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'price', 'stock_quantity']
    search_fields = ['name', 'category']
    ordering_fields = ['price', 'created_at']
    authentication_classes = [JWTAuthentication]  # Add JWT Authentication
    permission_classes = [IsAuthenticatedOrReadOnly]  # Only authenticated users can access

    def get_queryset(self):
        """
        Optionally filter products by category or name.
        """
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        name = self.request.query_params.get('name')
        
        if category:
            queryset = queryset.filter(category__icontains=category)
        if name:
            queryset = queryset.filter(name__icontains=name)
        
        return queryset

    def post(self, request, *args, **kwargs):
        """
        Create a new product. Restricted to authenticated users.
        """
        if not request.user.is_authenticated:
            return Response(
                {"detail": "Authentication credentials were not provided."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        
        serializer = ProductWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a single product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    lookup_field = 'id'

    def get_object(self):
        try:
            return super().get_object()
        except Product.DoesNotExist:
            raise NotFound("The requested product was not found.")
            
    def delete(self, request, *args, **kwargs):
        """
        Deletes a product and returns a success message.
        """
        product = self.get_object()
        product_name = product.name  # Optional: Capture product name for response message
        product.delete()
        return Response(
            {"detail": f"Product '{product_name}' has been successfully deleted."},
            status=status.HTTP_200_OK
        )

class ProductSearchView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination  # Use default pagination

    def get_queryset(self):
        """
        Override the default queryset to filter by name or category based on query params.
        """
        queryset = super().get_queryset()
        name = self.request.query_params.get('name', None)
        category = self.request.query_params.get('category', None)

        if name:
            queryset = queryset.filter(name__icontains=name)  # Partial match for name
        if category:
            queryset = queryset.filter(category__icontains=category)  # Partial match for category

        return queryset

class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
