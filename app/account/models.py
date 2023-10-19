from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.


class Address(models.Model):
    customer_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="customer_id",
        db_column="customer_id",
    )
    address_name = models.CharField(max_length=100, verbose_name="address_name")
    address = models.CharField(max_length=255, verbose_name="address")
    postcode = models.CharField(max_length=20)
    base_address = models.CharField(max_length=100)
    detail_address = models.CharField(max_length=50)
    extra_address = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def set_is_default(self):
        Address.objects.filter(customer_id=self.customer_id).update(is_default=False)
        self.is_default = True
        self.save()
