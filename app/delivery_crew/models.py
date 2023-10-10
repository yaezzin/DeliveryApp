from django.db import models
from django.contrib.auth.models import User
from sajjang.models import Order


class DeliveryLocation(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="customer_id"
    )  # ForiegnKey 파라미터의 첫번 째에 참조할 모델을 가져옵니다. 참조하고자 하는 모델(지금은 User) Import 필수입니다.
    longitude = models.FloatField()
    latitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class DeliveryHistory(models.Model):
    delivery_crew_id = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="delivery_crew"
    )
    order_id = models.ForeignKey(
        Order, on_delete=models.CASCADE, verbose_name="order_id"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class RejectedOrder(models.Model):
    delivery_crew_id = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="delivery_crew"
    )
    order_id = models.ForeignKey(
        Order, on_delete=models.CASCADE, verbose_name="order_id"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
