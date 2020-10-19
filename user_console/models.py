from django.db import models
from django.contrib.auth.models import User

# # Create your models here.
class Product(models.Model):
    
    # LINK TO USER 
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )
 
    # NAME OF PRODUCT
    name = models.CharField(
        max_length=60,
        blank=False
    )
    # COMPANY NAME
    company = models.CharField(
        max_length=60,
        default="Private Company",
        blank=False
    )
    # CATEGORY THE PRODUCT BELONG TO
    CATEGORY = [
        ('Formal-Wear','Formal-Wear'),
        ('Casual-Wear','Casual-Wear'),
        ('Accessories','Accessories'),
        ('Ties','Ties'),
    ]
    category = models.CharField(
        max_length=15,
        choices=CATEGORY,
        default='Formal-Wear',
        blank=False
    )
                                        
    # DESCRIPTION FOR THE PRODUCT
    description = models.TextField(
        max_length = 255
    )

    # CURRENT STOCK QUANTITY
    stock_qty = models.IntegerField(
        blank = False
    )
    
    # ORIGINAL PRICING OF PRODUCT TO BE SOLD
    price = models.DecimalField(
        blank=False,
        max_digits=5,
        decimal_places=2
    )

    def __str__(self):
        return (self.name)
    