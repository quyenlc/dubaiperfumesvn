from django.db import models
from django.conf import settings
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):

    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=800)
    info = models.TextField()
    star = models.FloatField(default=4.0)
    category = models.ForeignKey('Category', on_delete=models.PROTECT,
                                 default=1)  # Perfume
    image = models.ImageField(upload_to='products', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Landing(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='landings', null=True)

    def __str__(self):
        return self.title