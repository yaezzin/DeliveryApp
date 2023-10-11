from django.db import models
from django.contrib.auth.models import User
from sajjang.models import Menus, Order

from sajjang.models import Stores


# Create your models here.
class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user_id")
    store_id = models.ForeignKey(
        Stores, on_delete=models.CASCADE, verbose_name="store_id"
    )
    menu_id = models.ForeignKey(Menus, on_delete=models.CASCADE, verbose_name="menu_id")
    order_id = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name="order_id",
        null=True,
        default=None,
    )
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_total_price(self):
        return self.quantity * self.menu_id.unit_price
