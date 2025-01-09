from rest_framework import serializers
from .models import Product, Review, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Nested serializer to show category details
    reviews = serializers.SerializerMethodField()  # Custom field to display reviews
    is_in_stock = serializers.BooleanField(source='is_in_stock', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'stock_quantity', 'category', 
            'image_url', 'created_at', 'reviews', 'is_in_stock'
        ]

    def get_reviews(self, obj):
        """Retrieve the reviews for a product."""
        reviews = obj.reviews.all()
        return ReviewSerializer(reviews, many=True).data
        
class ProductWriteSerializer(serializers.ModelSerializer):
    """Serializer for creating and updating Product instances."""
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock_quantity', 'category', 'image_url']

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Display username instead of user ID

    class Meta:
        model = Review
        fields = ['id', 'user', 'rating', 'comment', 'created_at']
