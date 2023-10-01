from django.db import models

# # Create your models here.
# class Order(models.Model):
#     id = models.BigAutoField(help_text="Order ID", primary_key=True)
#     user_id = models.ForeignKey('User', related_name="user", on_delete=models.CASCADE, varbose_name="유저id")
#     total_price = models.IntegerField(verbose_name="총 금액")
#     create_time = models.DateTimeField(verbose_name="주문일자")
#     paid_status = models.BooleanField(default=False)
#     delivery_status = models.BooleanField(default=False)
#     receipt = models.CharField(max_length=100)


#     class Meta:
#         verbose_name = '주문'
#         verbose_name_plural = '주문'
