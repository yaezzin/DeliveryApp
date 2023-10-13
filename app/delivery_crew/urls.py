from django.urls import path
from .views import *

app_name = "delivery_crew"

urlpatterns = [
    path("home/", DeliveryCrewHomeView.as_view(), name="delivery_crew_home"),
    path(
        "delivery_history/",
        DeliveryCrewDeliveryHistory.as_view(),
        name="delivery_crew_history",
    ),
    path(
        "delivery_history/<int:order_id>/pickup/",
        DeliveryCrewDeliveryHistoryPickUp.as_view(),
        name="delivery_crew_pickup",
    ),
    path(
        "delivery_history/<int:order_id>/complete/",
        DeliveryCrewDeliveryHistoryComplete.as_view(),
        name="delivery_crew_complete",
    ),
    path(
        "<int:order_id>/accept/",
        DeliveryCrewAcceptView.as_view(),
        name="delivery_crew_accept",
    ),
    path(
        "<int:order_id>/deny/",
        DeliveryCrewDenyView.as_view(),
        name="delivery_crew_deny",
    ),
    path(
        "<int:user_id>/alarm/",
        DeliveryCrewAlarmView.as_view(),
        name="delivery_crew_alarm",
    ),
]
