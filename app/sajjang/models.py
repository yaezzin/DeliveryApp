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
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)


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
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ("created", "Created"),
        ("paid", "Paid"),
        ("sajjang_accepted", "Sajjang Accepted"),
        ("sajjang_rejected", "Sajjang Rejected"),
        ("crew_accepted", "Crew Accepted"),
        ("delivery_in_progress", "Delivery In Progress"),
        ("delivered", "Delivered"),
    ]

    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="user_id",
        related_name="customer_id",
    )
    store_id = models.ForeignKey(
        Stores, on_delete=models.CASCADE, verbose_name="store_id"
    )
    address_id = models.ForeignKey(
        Address, on_delete=models.CASCADE, verbose_name="address_id"
    )
    total_price = models.IntegerField(verbose_name="total_price")
    order_status = models.CharField(
        max_length=20,
        choices=ORDER_STATUS_CHOICES,
        default="created",
        verbose_name="order_status",
    )
    paid_status = models.BooleanField(
        null=True, default=None, verbose_name="paid_status"
    )
    receipt = models.CharField(
        default=None, null=True, max_length=100, verbose_name="receipt"
    )
    is_sajjang_accepted = models.BooleanField(
        null=True, default=None, verbose_name="is_sajjang_accepted"
    )
    crew_rejected_order = models.ManyToManyField(
        User,
        through="RejectedOrder",
        blank=True,
        verbose_name="crew_rejected_order",
        related_name="reject_crew_id",
    )
    delivery_status = models.BooleanField(
        null=True, default=None, verbose_name="delivery_status"
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)


class DeliveryHistory(models.Model):
    delivery_crew_id = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="delivery_crew"
    )
    order_id = models.ForeignKey(
        Order, on_delete=models.CASCADE, verbose_name="order_id"
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)


class RejectedOrder(models.Model):
    delivery_crew_id = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="delivery_crew"
    )
    order_id = models.ForeignKey(
        Order, on_delete=models.CASCADE, verbose_name="order_id"
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
