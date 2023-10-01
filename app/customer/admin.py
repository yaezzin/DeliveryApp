from django.contrib import admin
from .models import Customer, Address
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'email']

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'address_name', 'address', 'is_default']
