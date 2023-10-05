from django.db import models
from django.contrib.auth.models import User
from sajjang.models import Menus, Order

from sajjang.models import Stores


# Create your models here.
class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user_id")
    stores_id = models.ForeignKey(
        Stores, on_delete=models.CASCADE, verbose_name="stores_id"
    )
    menus_id = models.ForeignKey(
        Menus, on_delete=models.CASCADE, verbose_name="menus_id"
    )
    order_id = models.ForeignKey(
        Order, on_delete=models.CASCADE, verbose_name="order_id"
    )
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
