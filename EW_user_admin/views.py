from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm

# Create your views here.
def user_info (request):
    products = Product.objects.all()
    return render (request, 'user_info.template.html', {
        'products' : products
    })

def edit_info (request, product_id):
    product_to_be_edit = get_object_or_404(Product, pk=product_id)
    edit_form = ProductForm(instance=product_to_be_edit)
    return render (request, 'edit_info.template.html', {
        'form' : edit_form
    })