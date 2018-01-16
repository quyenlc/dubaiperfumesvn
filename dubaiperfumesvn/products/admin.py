from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ['name']

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('code','name','price','description','star')
    search_fields = ['code', 'name', 'description']

admin.site.register(Product, ProductAdmin)

