from django.urls import path
import cart.views

urlpatterns = [
    path('summary/', cart.views.view_cart, name='view_cart'),
]