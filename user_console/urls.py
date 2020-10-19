from django.urls import path
import user_console.views

urlpatterns = [
    path('', user_console.views.product_info, name='product_info'),
    path('edit/<product_id>', user_console.views.edit_product, name='edit_product'),
    path('add', user_console.views.add_product, name='add_product'),
    path('remove/<product_id>', user_console.views.remove_product, name='remove_product'),
]