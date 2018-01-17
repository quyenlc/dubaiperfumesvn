from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/index.html', context)