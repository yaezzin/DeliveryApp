from django.urls import path
from .views import *

app_name = "delivery_crew"

urlpatterns = [
    path("home/", DeliveryCrewHomeView.as_view(), name="deliverycrew_home"),
    path("<int:order_id>/accept/", DeliveryCrewAcceptView.as_view(), name="accept"),
    path("<int:order_id>/deny/", DeliveryCrewDenyView.as_view(), name="deny"),
    path("<int:user_id>/alarm/", DeliveryCrewAlarmView.as_view(), name="alarm"),
]
