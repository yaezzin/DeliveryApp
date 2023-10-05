from django.urls import path,
from .views import SajjangAddMenuView, SajjangHomeView, SajjangOrderView, SajjangStoreAddView, SajjangStoreDetailView, SajjangStoreMenuItemView, SajjangStoreMenuView, SajjangStoreOrderView, SajjangStoreView, SajjangOrderConfirmView


urlpatterns = [
    path("home", SajjangHomeView.as_view(), name="sajjang_home"),
    path("store", SajjangStoreView.as_view(), name="sajjang_store"),
    path("store/add", SajjangStoreAddView.as_view(), name="sajjang_store_add"),
    path("store/<int:store_id>", SajjangStoreDetailView.as_view(), name="sajjang_store_detail"),
    path("store/<int:store_id>/menu", SajjangStoreMenuView.as_view(), name="sajjang_store_menu"),
    path("store/<int:store_id>/menu/add", SajjangAddMenuView.as_view(), name="sajjang_add_menu"),
    path("store/<int:store_id>/menu/<int:menu_id>", SajjangStoreMenuItemView.as_view(), name="sajjang_store_menu_item"),
    path("store/<int:store_id>/order", SajjangStoreOrderView.as_view(), name="sajjang_store_order"),
    path("store/<int:store_id>/order/<int:order_id>", SajjangOrderView.as_view(), name="sajjang_order"),
    path("order/<int:order_id>/confirm", SajjangOrderConfirmView.as_view(), name="sajjang_order_confirm")
]
