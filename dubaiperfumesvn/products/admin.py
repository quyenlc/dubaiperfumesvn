from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ['name']

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('code','name','price', 'image', 'description','star')
    search_fields = ['code', 'name', 'description']

admin.site.register(Product, ProductAdmin)

class LandingAdmin(admin.ModelAdmin):
    list_display = ('title','description', 'image', 'created_at','updated_at')
    search_fields = ['title','description']

admin.site.register(Landing, LandingAdmin)
