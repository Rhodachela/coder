from rest_framework import serializers
from .models import Product, Review, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField()  # Accept a category name directly as a string

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'stock_quantity',
            'category',
            'image_url',
            'created_at',
            'is_in_stock',
        ]

    def create(self, validated_data):
        # Handle category creation or retrieval
        category_name = validated_data.pop('category')
        category, created = Category.objects.get_or_create(name=category_name)
        validated_data['category'] = category
        return super().create(validated_data)

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
