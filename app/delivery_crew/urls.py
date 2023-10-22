from django.urls import path
from .views import *

app_name = "delivery_crew"

urlpatterns = [
    path("home/", DeliveryCrewHomeView.as_view(), name="delivery_crew_home"),
    path("address/", DeliveryCrewAddressView.as_view(), name="delivery_crew_address"),
    path(
        "address/add/",
        DeliveryCrewAddressAddView.as_view(),
        name="delivery_crew_address_add",
    ),
    path(
        "address/<int:address_id>/",
        DeliveryCrewAddressDetailView.as_view(),
        name="delivery_crew_address_detail",
    ),
    path(
        "address/<int:address_id>/edit/",
        DeliveryCrewAddressEditView.as_view(),
        name="delivery_crew_address_edit",
    ),
    path(
        "address/<int:address_id>/delete/",
        DeliveryCrewAddressDeleteView.as_view(),
        name="delivery_crew_address_delete",
    ),
    path(
        "delivery_history/",
        DeliveryCrewDeliveryHistory.as_view(),
        name="delivery_crew_history",
    ),
    path(
        "delivery_history/<int:order_id>/",
        DeliveryHistoryDetailView.as_view(),
        name="delivery_history_detail",
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
