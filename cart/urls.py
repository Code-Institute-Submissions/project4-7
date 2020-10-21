from django.urls import path
import cart.views

urlpatterns = [
    path('summary/', cart.views.view_cart, name='view_cart'),
    path('add/<product_id>', cart.views.add_cart, name='add_cart'),
    path('remove/<product_id>', cart.views.remove_item, name='remove_item'),
    path('add_qty/<product_id>', cart.views.add_qty, name='add_qty'),
    path('minus_qty/<product_id>', cart.views.minus_qty, name='minus_qty'),
]