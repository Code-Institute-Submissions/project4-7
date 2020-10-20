from django.urls import path
import cart.views

urlpatterns = [
    path('summary/', cart.views.view_cart, name='view_cart'),
    path('add/<product_id>', cart.views.add_cart, name='add_cart'),
]