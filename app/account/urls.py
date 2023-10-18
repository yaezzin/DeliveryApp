from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required

from account.views import SigninView, SignupView, HomeView

app_name = "account"

urlpatterns = [
    path("signin/", SigninView.as_view(), name="signin"),
    path("signup/", SignupView.as_view(), name="signup"),
]
