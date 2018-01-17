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
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    description = models.TextField()
    info = models.TextField()
    star = models.FloatField(default=4.0)
    category = models.ForeignKey('Category', on_delete=models.PROTECT,
                                 default=1)  # Perfume
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Landing(models.Model):
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    titile = models.CharField(max_length=100)
    message = models.CharField(max_length=500)
    redirect_link = models.URLField()
