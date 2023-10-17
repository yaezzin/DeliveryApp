from django.db import models
from django.contrib.auth.models import User


class DeliveryLocation(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="customer_id", db_column="user_id"
    )  # ForiegnKey 파라미터의 첫번 째에 참조할 모델을 가져옵니다. 참조하고자 하는 모델(지금은 User) Import 필수입니다.
    active_area = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
