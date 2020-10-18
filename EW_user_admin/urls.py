from django.urls import path
import EW_user_admin.views

urlpatterns = [
    path('', EW_user_admin.views.product_info, name='product_info'),
    path('edit/<product_id>', EW_user_admin.views.edit_product, name='edit_product'),
    path('add', EW_user_admin.views.add_product, name='add_product'),
    path('remove/<product_id>', EW_user_admin.views.remove_product, name='remove_product'),
]