from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from account.views import (
    HomeView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("account.urls"), name="account"),
    path("", HomeView.as_view(), name="home"),
    # path("signin/", SigninView.as_view(), name="signin"),
    # path("signup/", SignupView.as_view(), name="signup"),
    path("customer/", include("customer.urls"), name="customer"),
    path("sajjang/", include("sajjang.urls"), name="sajjang"),
    path("delivery_crew/", include("delivery_crew.urls"), name="delivery_crew"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("", include("django_prometheus.urls")),
]
