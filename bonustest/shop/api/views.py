from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate, login as auth_login, logout as auth_logout
)
from ..models import Category, Product
from .serializers import (
    CategorySerializer, CategoryDetailSerializer, ProductListSerializer,
    ProductDetailSerializer, UserSerializer
)

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.views import Response


class CategoriesList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class ProductsList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class UserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


@api_view(['POST'])
def login(request):
    username = request.data.get('username', '')
    password = request.data.get('password', '')

    post_params = request.data

    user = authenticate(username=username, password=password)
    # user = None
    if user and user.is_active:
        auth_login(request, user)
        return Response({
            'success': True,
            'user': UserSerializer(request.user).data
        })
    else:
        return Response({
            'success': False,
            'reason': 'incorrect',
            'request': post_params,
            'username': username,
            'password': password
            })


@api_view(['GET'])
def logout(request):
    auth_logout(request._request)
    return Response({
        'success': True,
    })
