from django.urls import path, include
from rest_framework.routers import SimpleRouter

from example.views import ExampleView, CategoryView, UserView

router = SimpleRouter()

router.register('examples', ExampleView, basename='examples')
router.register('categories', CategoryView, basename='categories')
router.register('users', UserView, basename='users')

urlpatterns = [
    path('', include(router.urls))
]
