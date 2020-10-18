from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product
from .forms import ProductForm

# Create your views here.
def product_info (request):
    products = Product.objects.all()
    return render (request, 'product_info.template.html', {
        'products' : products
    })

def edit_product (request, product_id):
    product_to_be_edit = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        edit_form = ProductForm(request.POST, instance=product_to_be_edit)
        edit_form.save()
        return redirect(reverse(product_info))
    else:
        edit_form = ProductForm(instance=product_to_be_edit)
        return render (request, 'edit_product.template.html', {
            'form' : edit_form
        })

def add_product (request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        form.save()
        return redirect(reverse(product_info))
    else:
        form = ProductForm()
        return render (request, 'add_product.template.html', {
            'form' : form
        })

def remove_product(request, product_id):
    return render(request,'remove_product.template.html')
