from django.contrib import admin
from django.urls import path, include, re_path
from .swagger import urlpatterns as swagger_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/v1/', include(swagger_urls)),

    re_path(r'api/(?P<version>(v1))/', include('example.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

