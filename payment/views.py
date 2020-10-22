import stripe
from django.conf import settings
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from main_app.views import index
from payment.models import Payment_log

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
        # Update Log
    else:
        stripe.api_key = settings.STRIPE_SECRET_KEY 
        charge = stripe.Charge.create(
            amount= amount_to_charge,
            currency='sgd',
            description='Payment made for transaction',
            source=request.POST['stripeToken']
        )

        # Clear cart

        # Update Log
            
        return redirect(reverse('index'))