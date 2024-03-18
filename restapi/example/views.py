from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet

from example.models import ExampleModel, Category
from example.serializers import ExampleSerializer, CategorySerializer, UserSerializer


class ExampleView(ModelViewSet):
    queryset = ExampleModel.objects.all().select_related('category_id')
    serializer_class = ExampleSerializer


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserView(ModelViewSet):
    queryset = User.objects.all().prefetch_related('groups', 'user_permissions')
    serializer_class = UserSerializer
