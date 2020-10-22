from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product
from .forms import ProductForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main_app.views import index

# Create your views here.
@login_required
def product_info (request):
    # check for superuser else redirect back to index page
    if request.user.is_superuser:
        # find all products and show
        products = Product.objects.all()
        return render (request, 'product_info.template.html', {
            'products' : products
        })
    else:
        # return user to index
        return redirect(reverse(index))

@login_required
def edit_product (request, product_id):
    # check for superuser else redirect back to index page
    if request.user.is_superuser:
        # retrieve the product to be updated
        product_to_be_edit = get_object_or_404(Product, pk=product_id)

        if request.method == "POST":
            # load the updated form from the html
            edit_form = ProductForm(request.POST, instance=product_to_be_edit)
            if edit_form.is_valid():
                # process the form and save to database if it is valid
                updated_form = edit_form.save(commit=False)
                updated_form.user = product_to_be_edit.user
                updated_form.save()
                messages.success(request, f"The product {updated_form.name} has been updated")
                return redirect(reverse(product_info))
            else:
                # return to form if invalid form
                return render (request, 'edit_product.template.html', {
                    'form' : edit_form
                })
        else:
            # render the edit form with the data loaded in
            edit_form = ProductForm(instance=product_to_be_edit)
            return render (request, 'edit_product.template.html', {
                'form' : edit_form
            })
    else:
        # return user back to index
        return redirect(reverse(index))

@login_required
def add_product (request):
    # check for superuser else redirect back to index page
    if request.user.is_superuser:
        if request.method == "POST":
            # process form and save to database
            form = ProductForm(request.POST)
            new_product = form.save(commit=False)
            new_product.user = request.user
            new_product.save()
            messages.success(request, f"The product {new_product.name} has been added")
            return redirect(reverse(product_info))
        else:
            # render the form to html
            form = ProductForm()
            return render (request, 'add_product.template.html', {
                'form' : form
            })
    else:
        # return user back to index
        return redirect(reverse(index))

@login_required
def remove_product(request, product_id):
    # check for superuser else redirect back to index page
    if request.user.is_superuser:
        # get the product that is being updated
        product_to_be_remove = get_object_or_404(Product, pk=product_id)
        if request.method=="POST":
            # delete the product
            product_to_be_remove.delete()
            messages.success(request, f"The product {product_to_be_remove.name} has been removed")
            return redirect(reverse(product_info))
        else:        
            # render the delete form to confirm deletion
            return render(request,'remove_product.template.html', {
                'product' : product_to_be_remove
            })
    else:
        # return user back to index
        return redirect(reverse(index))