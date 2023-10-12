from django.urls import path
from .views import *

app_name = "sajjang"

# realted to Main & Store
urlpatterns = [
    path("home/", SajjangHomeView.as_view(), name="sajjang_home"),
    path("store/add", SajjangStoreAddView.as_view(), name="sajjang_store_add"),
    path(
        "store/<int:store_id>",
        SajjangStoreDetailView.as_view(),
        name="sajjang_store_detail",
    ),
    path(
        "store/<int:store_id>/edit",
        SajjangStoreEditView.as_view(),
        name="sajjang_store_edit",
    ),
    path(
        "store/<int:store_id>/delete",
        SajjangStoreDeleteView.as_view(),
        name="sajjang_store_delete",
    ),
]

# related to Menu
urlpatterns += [
    path(
        "store/<int:store_id>/menu",
        SajjangStoreMenuView.as_view(),
        name="sajjang_store_menu",
    ),
    path(
        "store/<int:store_id>/menu/add",
        SajjangAddMenuView.as_view(),
        name="sajjang_add_menu",
    ),
    path(
        "store/<int:store_id>/menu/<int:menu_id>",
        SajjangStoreMenuDetailView.as_view(),
        name="sajjang_store_menu_detail",
    ),
    path(
        "store/<int:store_id>/menu/<int:menu_id>/edit",
        SajjangMenuEditView.as_view(),
        name="sajjang_store_menu_edit",
    ),
    path(
        "store/<int:store_id>/menu/<int:menu_id>/delete",
        SajjangMenuDeleteView.as_view(),
        name="sajjang_store_menu_delete",
    ),
]

# related to Order
urlpatterns += [
    path(
        "store/<int:store_id>/order",
        SajjangOrdersView.as_view(),
        name="sajjang_store_order",
    ),
    path(
        "store/<int:store_id>/order/<int:order_id>",
        SajjangOrderDetailView.as_view(),
        name="sajjang_order_detail",
    ),
    path(
        "store/<int:store_id>/order/confirm",
        SajjangOrderConfirmView.as_view(),
        name="sajjang_order_confirm",
    ),
    path(
        "store/<int:store_id>/order/confirm/<int:order_id>/accept",
        SajjangOrderAcceptView.as_view(),
        name="sajjang_order_accept",
    ),
    path(
        "store/<int:store_id>/order/confirm/<int:order_id>/reject",
        SajjangOrderRejectView.as_view(),
        name="sajjang_order_reject",
    ),
]
