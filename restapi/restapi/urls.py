from django.contrib import admin
from django.urls import path, include
from .swagger import urlpatterns as swagger_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(swagger_urls)),

    path('api/v1/', include('example.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

