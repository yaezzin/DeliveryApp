from django.db import models

# Create your models here.
class Menus(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='category_id')
    name = models.CharField(max_length=128)
    unit_price = models.IntegerField()
    menu_pic = models.ImageField()
    is_available = models.BooleanField()