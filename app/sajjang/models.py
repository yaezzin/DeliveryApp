from django.db import models
from django.contrib.auth.models import User
from account.models import Address


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="name")


class Stores(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    store_pic = models.ImageField(blank=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)


class Menus(models.Model):
    store_id = models.ForeignKey(
        Stores, on_delete=models.CASCADE, verbose_name="store_id", null=True
    )
    category_id = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="category_id", null=True
    )
    name = models.CharField(max_length=128)
    unit_price = models.IntegerField()
    menu_pic = models.ImageField(blank=True)
    is_available = models.BooleanField()


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user_id")
    store_id = models.ForeignKey(
        Stores, on_delete=models.CASCADE, verbose_name="store_id"
    )
    address_id = models.ForeignKey(
        Address, on_delete=models.CASCADE, verbose_name="address_id"
    )
    total_price = models.IntegerField(verbose_name="total_price")
    create_time = models.DateTimeField(auto_now_add=True)
    paid_status = models.BooleanField(
        null=True, default=None, verbose_name="paid_status"
    )
    delivery_status = models.BooleanField(
        null=True, default=None, verbose_name="delivery_status"
    )
    is_sajjang_accepted = models.BooleanField(
        null=True, default=None, verbose_name="is_sajjang_accepted"
    )
    receipt = models.CharField(
        default=None, null=True, max_length=100, verbose_name="receipt"
    )
