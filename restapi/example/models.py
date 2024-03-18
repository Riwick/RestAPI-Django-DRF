from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, null=False)


class ExampleModel(models.Model):
    title = models.CharField(max_length=255, null=False)
    age = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1.00)
    description = models.TextField(max_length=2000, null=True)
    category_id = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    author_id = models.ManyToManyField(User)
