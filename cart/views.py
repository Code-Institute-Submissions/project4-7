from django.shortcuts import render

# Create your views here.
def view_cart(request):
    return render (request, 'view_cart.template.html')

def add_cart(request, product_id):
    return render (request, 'add_cart.template.html')