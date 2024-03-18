from django.urls import path, include
from rest_framework.routers import SimpleRouter

from example.views import ExampleView, CategoryView, UserView

router = SimpleRouter()

router.register('examples', ExampleView)
router.register('categories', CategoryView)
router.register('users', UserView)

urlpatterns = [
    path('', include(router.urls))
]
