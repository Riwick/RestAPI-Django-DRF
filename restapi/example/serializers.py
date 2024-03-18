from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from example.models import ExampleModel, Category


class ExampleSerializer(ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'date_joined')
