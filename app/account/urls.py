from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
import account.views as account

app_name = "account"

urlpatterns = [

]

