from django.urls import path
import EW_user_admin.views

urlpatterns = [
    path('', EW_user_admin.views.user_info, name='user_info'),
    path('edit/<product_id>', EW_user_admin.views.edit_info, name='edit_info'),
]