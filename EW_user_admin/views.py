from django.shortcuts import render, get_object_or_404, redirect, reverse
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
    if request.method == "POST":
        edit_form = ProductForm(request.POST, instance=product_to_be_edit)
        edit_form.save()
        return redirect(reverse(user_info))
    else:
        edit_form = ProductForm(instance=product_to_be_edit)
        return render (request, 'edit_info.template.html', {
            'form' : edit_form
        })