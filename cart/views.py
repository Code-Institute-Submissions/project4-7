from django.shortcuts import render, get_object_or_404, redirect, reverse
from user_console.models import Product
from django.contrib import messages
from main_app.views import shop

# Create your views here.
def view_cart(request):
    cart = request.session.get('shopping_cart', {})
    final_cost = 0
    # Calculate the final total costing for the charge
    for item in cart:
        final_cost = final_cost+ float(cart[item]['item_total_cost'])
        
    # convert to string to display decimals in html
    final_cost = format(float(final_cost),'.2f')

    return render (request, 'view_cart.template.html', {
        'cart': cart,
        'final_cost' : final_cost
    })

def add_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    # if there is available stock then add to cart
    if product.stock_qty > 0:
        # load cart detail
        cart = request.session.get('shopping_cart', {})
        # check whether the product_is not in the cart. else we will add it
        if product_id not in cart:            
            # product is found, let's add it to the cart
            cart[product_id] = {
                'id': product_id,
                'name': product.name,
                'price': format(float(product.price),'.2f'),
                'qty' : 1,
                'item_total_cost' : format(float(product.price),'.2f'),
            }
            # save the cart back to sessions
            request.session['shopping_cart'] = cart
            messages.success(request, "product has been added to your cart!")
        else:
            cart[product_id]['qty'] +=1  
            item_total_cost = cart[product_id]['qty'] * float(cart[product_id]['price']) 
            cart[product_id]['item_total_cost'] = format(float(item_total_cost),'.2f')          
            # save the cart back to sessions
            request.session['shopping_cart'] = cart

    return redirect('shop', category='All')


def remove_item (request, product_id):
    cart = request.session.get('shopping_cart', {})
    # Check if product exist in cart then remove it
    if product_id in cart:
        del cart[product_id]
        request.session['shopping_cart'] = cart

    return redirect(reverse('view_cart'))

def add_qty (request, product_id):
    cart = request.session.get('shopping_cart', {})
    cart[product_id]['qty'] += 1
    item_total_cost = cart[product_id]['qty'] * float(cart[product_id]['price']) 
    cart[product_id]['item_total_cost'] = format(float(item_total_cost),'.2f') 

    request.session['shopping_cart'] = cart
    return redirect(reverse('view_cart'))

def minus_qty (request, product_id):
    cart = request.session.get('shopping_cart', {})
    if cart[product_id]['qty'] == 1 :
        del cart[product_id]
        request.session['shopping_cart'] = cart
        return redirect(reverse('view_cart'))
    else:
        cart[product_id]['qty'] -= 1
        item_total_cost = cart[product_id]['qty'] * float(cart[product_id]['price']) 
        cart[product_id]['item_total_cost'] = format(float(item_total_cost),'.2f') 
        
        request.session['shopping_cart'] = cart
        return redirect(reverse('view_cart'))