from django.db import models
from django.contrib.auth.models import User


class DeliveryLocation(models.Model):
    # ForiegnKey 파라미터의 첫번 째에 참조할 모델을 가져옵니다. 참조하고자 하는 모델(지금은 User) Import 필수입니다.
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="crew_id",
        db_column="user_id",
    )
    address_name = models.CharField(max_length=100, verbose_name="location_name")
    address = models.CharField(max_length=200)
    active_area = models.BooleanField(default=False)
    postcode = models.CharField(max_length=20)
    base_address = models.CharField(max_length=100)
    detail_address = models.CharField(max_length=50)
    extra_address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def set_is_default(self):
        DeliveryLocation.objects.filter(user_id=self.user_id).update(active_area=False)
        self.active_area = True
        self.save()
