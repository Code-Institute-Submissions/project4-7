import stripe
from django.conf import settings
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from main_app.views import index
from payment.models import Payment_log
from user_console.models import Product
from user_console.forms import ProductForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def checkout(request):
    cart = request.session.get("shopping_cart", {})
    amount = 0
    # load in amount to be charged
    for item in cart:
        amount = amount + float(cart[item]['item_total_cost'])
    # convert to string for passing to template (html)
    final_cost = format(float(amount),'.2f')
    # convert to int for charging by stripe
    amount = int(amount * 100)

    if request.method == 'GET':
        key = settings.STRIPE_PUBLISHABLE_KEY
        return render(request, 'checkout.template.html', {
            'key' : key,
            'amount' : amount,
            'cart' : cart,
            'final_cost' : final_cost,
        })
    else:
        stripe.api_key = settings.STRIPE_SECRET_KEY 
        charge = stripe.Charge.create(
            amount= amount,
            currency='sgd',
            description='Payment made for transaction',
            source=request.POST['stripeToken']
        )

        # Clear cart
        request.session['shopping_cart'] = {}

        # Set the transaction reference number 
        log = Payment_log.objects.latest('id')
        # print (log.id, log.transaction_reference)
        new_log = log.transaction_reference + 1

        for item_id in cart:
            # Update Product Remaining Quantity
            product_to_update = get_object_or_404(Product, pk=item_id)
        
            product_to_update.stock_qty = product_to_update.stock_qty - cart[item_id]['qty']
            product_to_update.save()

            # Update Log
            transaction_log = Payment_log(
                user = request.user,
                name = product_to_update.name,
                purchase_qty = cart[item_id]['qty'],
                purchase_price = cart[item_id]['price'],
                transaction_status = "Completed",
                transaction_reference = new_log,
            )
            transaction_log.save()
            
        return redirect(reverse('index'))

@login_required
def view_log (request):
    # check for superuser else redirect back to index page
    if request.user.is_superuser:
        transaction_history = Payment_log.objects.all()
        return render (request, 'view_log.template.html', {
            'transaction_history' : transaction_history,
        })
    else:
        # return user back to index
        return redirect(reverse(index))