from itertools import product
from django.contrib.auth.models import User
from django.db import models

from product.models import Produto

# Create your models here.
class Order(models.Model):
    ORDERED = 'ordered'
    SHIPPED = 'shipped'
    
    STATUS_CHOICES = (
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped')
    )
    
    user = models.ForeignKey(User, related_name='ordes', blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
        
    created_at = models.DateTimeField(auto_now_add=True)
    
    paid = models.BooleanField(default=False)
    paid_amount = models.IntegerField(blank=True, null=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ORDERED)

    class Meta:
        verbose_name = ("Order")
        verbose_name_plural = ("Orders")

    def __str__(self):
        return self.name


class OrderItem(models.Model):

    order = models.ForeignKey(Order, related_name='itens', on_delete=models.CASCADE)    
    produto = models.ForeignKey(Produto, related_name='itens', on_delete=models.CASCADE)
    price = models.IntegerField(default=1)
    quantidade = models.IntegerField(default=1)
    
    class Meta:
        verbose_name = ("OrderItem")
        verbose_name_plural = ("OrderItens")

    def __str__(self):
        return self.name


