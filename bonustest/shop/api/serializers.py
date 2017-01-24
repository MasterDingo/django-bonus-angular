from rest_framework import serializers

from django.contrib.auth.models import User

from ..models import Category, Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "price")


class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False)

    class Meta:
        model = Product
        fields = ("id", "category", "name", "description", "price")


class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = "__all__"
