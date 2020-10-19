from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product
from .forms import ProductForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def product_info (request):
    products = Product.objects.all()
    return render (request, 'product_info.template.html', {
        'products' : products
    })

@login_required
def edit_product (request, product_id):

    product_to_be_edit = get_object_or_404(Product, pk=product_id)
    # edit_form = ProductForm(request.POST, instance=product_to_be_edit)

    if request.method == "POST":
        edit_form = ProductForm(request.POST, instance=product_to_be_edit)
        if edit_form.is_valid():
            updated_form = edit_form.save(commit=False)
            updated_form.user = product_to_be_edit.user
            updated_form.save()
            messages.success(request, f"The product {updated_form.name} has been updated")
            return redirect(reverse(product_info))
        else:
            # edit_form = ProductForm(instance=product_to_be_edit)
            return render (request, 'edit_product.template.html', {
                'form' : edit_form
            })
    else:
        edit_form = ProductForm(instance=product_to_be_edit)
        return render (request, 'edit_product.template.html', {
            'form' : edit_form
        })

@login_required
def add_product (request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        new_product = form.save(commit=False)
        new_product.user = request.user
        new_product.save()
        messages.success(request, f"The product {new_product.name} has been added")
        return redirect(reverse(product_info))
    else:
        form = ProductForm()
        return render (request, 'add_product.template.html', {
            'form' : form
        })

@login_required
def remove_product(request, product_id):
    product_to_be_remove = get_object_or_404(Product, pk=product_id)
    if request.method=="POST":
        product_to_be_remove.delete()
        messages.success(request, f"The product {product_to_be_remove.name} has been removed")
        return redirect(reverse(product_info))
    else:        
        return render(request,'remove_product.template.html', {
            'product' : product_to_be_remove
        })
