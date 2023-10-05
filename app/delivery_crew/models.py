from django.db import models
from django.contrib.auth.models import User

class DeliveryLocation(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='customer_id') #ForiegnKey 파라미터의 첫번 째에 참조할 모델을 가져옵니다. 참조하고자 하는 모델(지금은 User) Import 필수입니다.
	longitude = models.FloatField(max_digits=9, decimal_places=6)
	latitude = models.FloatField(max_digits=8, decimal_places=6)