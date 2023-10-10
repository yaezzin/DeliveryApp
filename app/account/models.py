from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.


class Address(models.Model):
    customer_id = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="customer_id"
    )
    address_name = models.CharField(max_length=100, verbose_name="address_name")
    address = models.CharField(max_length=255, verbose_name="address")
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
