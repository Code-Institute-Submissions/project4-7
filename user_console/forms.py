from django import forms
from .models import Product
from cloudinary.forms import CloudinaryJsFileField

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'company',
            'name', 
            'category', 
            'description', 
            'stock_qty',
            'price',
            'cover'
            )
    cover = CloudinaryJsFileField()
    