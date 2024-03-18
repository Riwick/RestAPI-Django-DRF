from django.contrib import admin

from example.models import ExampleModel, Category

admin.site.register(ExampleModel)
admin.site.register(Category)
