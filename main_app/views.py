from django.shortcuts import render
from user_console.models import Product
# Create your views here.
def index(request):
    return render(request,'index.template.html')

def shop(request):
    products = Product.objects.all()
    return render(request,'shop.template.html', {
        'products' : products
    })

def display_category(request, category):
    products = Product.objects.filter(category=category)
    return render(request,'shop.template.html', {
        'products' : products
    })