from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=150, unique=True, verbose_name='Username')
    password = models.CharField(max_length=128, verbose_name='Password')
    email = models.EmailField(max_length=255, unique=True, verbose_name='Email')

class Address(models.Model):
    customer_id = models.ForeignKey('Customer', related_name='customer', on_delete=models.CASCADE)
    address_name = models.CharField(max_length=100, verbose_name='address_name')
    address = models.CharField(max_length=255, verbose_name='Address')
    is_default = models.BooleanField(default=False)
