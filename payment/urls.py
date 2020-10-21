from django.urls import path
import payment.views

urlpatterns = [
    path('', payment.views.checkout, name='checkout'),
    
]