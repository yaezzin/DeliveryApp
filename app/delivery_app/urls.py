"""
URL configuration for delivery_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from account.views import (
    SigninView,
    SignupView,
    CustomerView,
    SajjangView,
    DeliveryCrewView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", SigninView.as_view(), name="signin"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("customer/", include("customer.urls"), name="customer"),
    path("sajjang/", include("sajjang.urls"), name="sajjang"),
    path("delivery_crew/", include("delivery_crew.urls"), name="delivery_crew"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("", include("django_prometheus.urls")),
]
