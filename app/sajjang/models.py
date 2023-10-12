from django.db import models
from django.contrib.auth.models import User
from account.models import Address


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="name")


class Stores(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user_id")
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    store_pic = models.ImageField(blank=True)
    category_id = models.ForeignKey(
        Category, on_delete=models.CASCADE, db_column="category_id"
    )
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)


class Menus(models.Model):
    store_id = models.ForeignKey(
        Stores,
        on_delete=models.CASCADE,
        verbose_name="store_id",
        null=True,
        db_column="store_id",
    )
    category_id = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="category_id",
        null=True,
        db_column="category_id",
    )
    name = models.CharField(max_length=128)
    unit_price = models.IntegerField()
    menu_pic = models.ImageField(blank=True)
    is_available = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ("created", "Created"),  # 오더가 처음으로 생성되었을 때
        ("paid", "Paid"),  # 결제가 완료 되었을 때
        ("sajjang_accepted", "Sajjang Accepted"),  # 사장이 수락했을 때
        ("sajjang_rejected", "Sajjang Rejected"),  # 사정이 거절했을 때
        ("crew_accepted", "Crew Accepted"),  # 배달 크루가 수락했을 때
        ("delivery_in_progress", "Delivery In Progress"),  # 배달 픽업이 되었을 때
        ("delivered", "Delivered"),  # 배달이 완료 되었을 때
    ]

    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="user_id",
        related_name="customer_id",
        db_column="user_id",
    )
    store_id = models.ForeignKey(
        Stores, on_delete=models.CASCADE, verbose_name="store_id", db_column="store_id"
    )
    address_id = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        verbose_name="address_id",
        db_column="address_id",
    )
    total_price = models.IntegerField(verbose_name="total_price")
    order_status = models.CharField(
        max_length=20,
        choices=ORDER_STATUS_CHOICES,
        default="created",
        verbose_name="order_status",
    )
    # paid_status = models.BooleanField(
    #     null=True, default=None, verbose_name="paid_status"
    # )
    receipt = models.CharField(
        default=None, null=True, max_length=100, verbose_name="receipt"
    )
    # is_sajjang_accepted = models.BooleanField(
    #     null=True, default=None, verbose_name="is_sajjang_accepted"
    # )
    crew_rejected_order = models.ManyToManyField(
        User,
        through="RejectedOrder",
        blank=True,
        verbose_name="crew_rejected_order",
        related_name="reject_crew_id",
        db_column="crew_rejected_order",
    )
    # delivery_status = models.BooleanField(
    #     null=True, default=None, verbose_name="delivery_status"
    # )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderStatusHistory(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=25, choices=Order.ORDER_STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


class DeliveryHistory(models.Model):
    delivery_crew_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="delivery_crew",
        db_column="delivery_crew_id",
    )
    order_id = models.ForeignKey(
        Order, on_delete=models.CASCADE, verbose_name="order_id", db_column="order_id"
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)


class RejectedOrder(models.Model):
    delivery_crew_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="delivery_crew",
        db_column="delivery_crew_id",
    )
    order_id = models.ForeignKey(
        Order, on_delete=models.CASCADE, verbose_name="order_id", db_column="order_id"
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
