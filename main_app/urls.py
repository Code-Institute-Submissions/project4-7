from django.urls import path
import main_app.views

urlpatterns = [
    path('', main_app.views.index, name='index'),
    path('shop/', main_app.views.shop, name='shop'),
]