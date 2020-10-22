from django.db import models
from django.contrib.auth.models import User
from user_console.models import Product

# Create your models here.
class Payment_log (models.Model):
    # Track the user making purchase
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )
    # Track the product purchase
    name = models.CharField(
        max_length=60,
        blank=False
    )
    # Track purchase quantity
    purchase_qty = models.IntegerField(
        blank=False
    )
    # Track purchase price
    purchase_price = models.DecimalField(
        blank=False,
        max_digits=5,
        decimal_places=2
    )
    # Track if transaction is successful
    transaction_status = models.CharField(
        max_length=10
    )
    # Track the timestamp of transaction
    timestamp = models.DateTimeField(
        auto_now_add=True
    )