from django.shortcuts import render, HttpResponse
from .models import Product

# Create your views here.
def user_info (request):
    products = Product.objects.all()
    return render (request, 'user_info.template.html', {
        'products' : products
    })

def edit_info (request):
    return render (request, 'edit_info.template.html')