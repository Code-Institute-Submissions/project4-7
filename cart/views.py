from django.shortcuts import render, get_object_or_404, redirect, reverse
from user_console.models import Product
from django.contrib import messages

# Create your views here.
def view_cart(request):
    cart = request.session.get('shopping_cart', {})
    return render (request, 'view_cart.template.html', {
        'cart': cart,
    })

def add_cart(request, product_id):
    # load cart detail
    cart = request.session.get('shopping_cart', {})
    # check whether the product_is not in the cart. else we will add it
    if product_id not in cart:
        product = get_object_or_404(Product, pk=product_id)
        # product is found, let's add it to the cart

        cart[product_id] = {
            'id': product_id,
            'name': product.name,
            'price': float(product.price),
            'qty' : 1,
        }

        # save the cart back to sessions
        request.session['shopping_cart'] = cart
        messages.success(request, "product has been added to your cart!")
        # return redirect(reverse('view_cart'))
    else:
        cart[product_id]['qty'] +=1        
        # save the cart back to sessions
        request.session['shopping_cart'] = cart

        # return HttpResponse('Product added')
    return redirect(reverse('view_cart'))