from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Product, Landing

# Create your views here.
def index(request):
    products = Product.objects.all()
    landings = Landing.objects.all()
    template = loader.get_template('products/index.html')
    context = {
        'products': products,
        'landings': landings,
    }
    return HttpResponse(template.render(context, request))

def detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    template = loader.get_template('products/detail.html')
    context = {
        'product': product,
    }
    return HttpResponse(template.render(context, request))