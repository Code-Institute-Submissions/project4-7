from django.urls import path
import payment.views

urlpatterns = [
    path('', payment.views.checkout, name='checkout'),
    path('view_log/', payment.views.view_log, name='view_log'),
]