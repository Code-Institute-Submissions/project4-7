import stripe
from django.conf import settings
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from main_app.views import index
from payment.models import Payment_log
from user_console.models import Product
from user_console.forms import ProductForm

# Create your views here.
def checkout(request):
    cart = request.session.get("shopping_cart", {})

    amount_to_charge = 100
    if request.method == 'GET':
        amount = amount_to_charge 
        key = settings.STRIPE_PUBLISHABLE_KEY
        return render(request, 'checkout.template.html', {
            'key' : key,
            'amount' : amount,
            'cart' : cart,
        })
    else:
        stripe.api_key = settings.STRIPE_SECRET_KEY 
        charge = stripe.Charge.create(
            amount= amount_to_charge,
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

def view_log (request):
    transaction_history = Payment_log.objects.all()
    return render (request, 'view_log.template.html', {
        'transaction_history' : transaction_history,
    })