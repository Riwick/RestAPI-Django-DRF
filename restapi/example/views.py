from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import *

from example.models import ExampleModel, Category
from example.permissions import IsAuthorOrReadOnly, IsAdminOrStaffOrReadOnly, IsUserOrReadOnly
from example.serializers import ExampleSerializer, CategorySerializer, UserSerializer

DEFAULT_PAGE_SIZE = 10


class Paginator(PageNumberPagination):
    page_size = DEFAULT_PAGE_SIZE
    page_query_param = 'page'
    display_page_controls = True


class ExampleView(ModelViewSet):
    queryset = ExampleModel.objects.all().select_related('category_id')
    serializer_class = ExampleSerializer

    pagination_class = Paginator
    permission_classes = [IsAuthorOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category_id', 'author_id', 'price']
    search_fields = ['title', 'age']
    ordering_fields = ['id', 'title', 'price', 'age']


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    pagination_class = Paginator
    permission_classes = [IsAdminOrStaffOrReadOnly]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id', 'title']
    ordering_fields = ['id', 'title']


class UserView(ModelViewSet):
    queryset = User.objects.all().prefetch_related('groups', 'user_permissions')
    serializer_class = UserSerializer

    pagination_class = Paginator
    permission_classes = [IsUserOrReadOnly, IsAuthenticatedOrReadOnly]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id', 'username']
    ordering_fields = ['id', 'date_joined']

