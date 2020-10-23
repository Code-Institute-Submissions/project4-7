from django.urls import path
import main_app.views

urlpatterns = [
    path('', main_app.views.index, name='index'),
    path('shop/<category>/', main_app.views.shop, name='shop'),
    # path('display_category/<category>/', main_app.views.display_category, name='display_category'),
]