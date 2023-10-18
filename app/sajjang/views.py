from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.contrib.auth.models import User

from .models import Stores, Menus, Category, Order
from customer.models import Cart
from common.utils import SajjangRequiredMixin, image_handler


def is_sajjang(user):
    return user.group.filter(name="sajjang").exists()


# /sajjang/home
class SajjangHomeView(SajjangRequiredMixin, TemplateView):
    template_name = "/app/sajjang/templates/home.html"

    def get(self, request):
        stores = Stores.objects.filter(user_id=request.user.id)
        context = {"stores": stores}
        return render(request, self.template_name, context)


# /sajjang/store/add
class SajjangStoreAddView(SajjangRequiredMixin, TemplateView):
    template_name = "/app/sajjang/templates/stores/add.html"

    def get(self, request):
        categories = Category.objects.all()
        context = {
            "categories": categories,
            "user": request.user.id,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        image_url = image_handler(request)

        try:
            name = request.POST["store_name"]
            address = request.POST["store_address"]
            store_pic = image_url if request.FILES.get("store_pic") else None
            status = request.POST.get("status", False)

            user = get_object_or_404(User, id=request.user.pk)
            category = get_object_or_404(Category, id=request.POST["category"])

            new_store = Stores(
                user_id=user,
                name=name,
                address=address,
                store_pic=store_pic,
                category_id=category,
                status=status,
            )
            new_store.save()

            return redirect("sajjang:sajjang_home")
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


# sajjang/store/<int:store_id>
class SajjangStoreDetailView(SajjangRequiredMixin, TemplateView):
    template_name = "/app/sajjang/templates/stores/store/detail.html"

    def get(self, request, store_id):
        store = get_object_or_404(Stores, id=store_id)
        context = {"store": store}
        return render(request, self.template_name, context)


# sajjang/store/<int:store_id>/edit
class SajjangStoreEditView(SajjangRequiredMixin, TemplateView):
    template_name = "/app/sajjang/templates/stores/store/edit.html"

    def get(self, request, store_id):
        store = get_object_or_404(Stores, id=store_id)
        categories = Category.objects.all()
        selected_category = store.category_id
        context = {
            "store": store,
            "categories": categories,
            "selected_category": selected_category,
        }
        return render(request, self.template_name, context)

    def post(self, request, store_id):
        try:
            store = get_object_or_404(Stores, id=store_id)
            exsiting_post = store.store_pic
            image_url = image_handler(request, exsiting_post)

            store.name = request.POST.get("name", store.name)
            store.address = request.POST.get("address", store.address)
            store.store_pic = image_url
            store.status = request.POST.get("status", False)
            store.category_id = Category.objects.get(id=request.POST["category"])
            store.save()
            return redirect("sajjang:sajjang_store_detail", store_id=store_id)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


# sajjang/store/<int:store_id>/delete
class SajjangStoreDeleteView(SajjangRequiredMixin, TemplateView):
    def post(self, request, store_id):
        try:
            store = get_object_or_404(Stores, id=store_id)
            store.delete()
            return redirect("sajjang:sajjang_home")
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


# sajjang/store/<int:store_id>/menu
class SajjangStoreMenuView(SajjangRequiredMixin, TemplateView):
    template_name = "/app/sajjang/templates/stores/store/menu/list.html"

    def get(self, request, store_id):
        store = get_object_or_404(Stores, id=store_id)
        menus = Menus.objects.filter(store_id=store_id)
        context = {"store": store, "menus": menus}
        return render(request, self.template_name, context)


# sajjang/store/<int:store_id>/menu/add
class SajjangAddMenuView(SajjangRequiredMixin, TemplateView):
    template_name = "/app/sajjang/templates/stores/store/menu/add.html"

    def get(self, request, store_id):
        store = get_object_or_404(Stores, id=store_id)
        categories = Category.objects.all()
        context = {"store": store, "categories": categories}
        return render(request, self.template_name, context)

    def post(self, request, store_id):
        print(request.FILES.get("menu_pic"))
        image_url = image_handler(request)

        try:
            store = Stores.objects.get(id=store_id)
            category = Category.objects.get(id=request.POST["category"])
            name = request.POST.get("name")
            unit_price = request.POST.get("unit_price")
            menu_pic = image_url if request.FILES.get("menu_pic") else None
            is_available = request.POST.get("is_available", False)

            new_menu = Menus(
                store_id=store,
                category_id=category,
                name=name,
                unit_price=unit_price,
                menu_pic=menu_pic,
                is_available=is_available,
            )

            new_menu.save()
            return redirect("sajjang:sajjang_store_menu", store_id=store.pk)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


# sajjang/store/<int:store_id>/menu/<int:menu_id>
class SajjangStoreMenuDetailView(SajjangRequiredMixin, TemplateView):
    template_name = "/app/sajjang/templates/stores/store/menu/detail.html"

    def get(self, request, store_id, menu_id):
        store = get_object_or_404(Stores, id=store_id)
        menu = get_object_or_404(Menus, id=menu_id)
        context = {"store": store, "menu": menu}
        return render(request, self.template_name, context)


# sajjang/store/<int:store_id>/menu/<int:menu_id>/edit
class SajjangMenuEditView(SajjangRequiredMixin, TemplateView):
    template_name = "/app/sajjang/templates/stores/store/menu/edit.html"

    def get(self, request, store_id, menu_id):
        menu = get_object_or_404(Menus, id=menu_id)
        categories = Category.objects.all()
        selected_category = menu.category_id
        context = {
            "menu": menu,
            "categories": categories,
            "selected_category": selected_category,
        }
        return render(request, self.template_name, context)

    def post(self, request, store_id, menu_id):
        try:
            menu = get_object_or_404(Menus, id=menu_id)
            exsiting_post = menu.menu_pic
            image_url = image_handler(request, exsiting_post)

            menu.category_id = Category.objects.get(id=request.POST["category"])
            menu.name = request.POST["name"]
            menu.unit_price = request.POST["unit_price"]
            menu.menu_pic = image_url
            menu.is_available = request.POST.get("is_available", False)
            menu.save()
            return redirect(
                "sajjang:sajjang_store_menu_detail", store_id=store_id, menu_id=menu_id
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


# sajjang/store/<int:store_id>/menu/<int:menu_id>/delete
class SajjangMenuDeleteView(SajjangRequiredMixin, TemplateView):
    def post(self, request, store_id, menu_id):
        try:
            menu = get_object_or_404(Menus, id=menu_id)
            menu.delete()
            return redirect("sajjang:sajjang_store_menu", store_id=store_id)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


# sajjang/store/<int:store_id>/order
class SajjangOrdersView(SajjangRequiredMixin, TemplateView):
    template_name = "/app/sajjang/templates/stores/orders/list.html"

    def get(self, request, store_id):
        selected_order_status = [
            "sajjang_accepted",
            "crew_accepted",
            "delivery_in_progress",
            "delivered",
        ]
        store = Stores.objects.get(id=store_id)
        orders = Order.objects.filter(
            store_id=store_id, order_status__in=selected_order_status
        )
        context = {"store": store, "orders": orders}
        return render(request, self.template_name, context)


# sajjang/store/<int:store_id>/order/<int:order_id>
class SajjangOrderDetailView(SajjangRequiredMixin, TemplateView):
    template_name = "/app/sajjang/templates/stores/orders/detail.html"

    def get(self, request, store_id, order_id):
        store = Stores.objects.get(id=store_id)
        order = get_object_or_404(Order, id=order_id)
        cart_in_order = Cart.objects.filter(order_id=order_id)
        context = {
            "store": store,
            "order": order,
            "cart_in_order": cart_in_order,
        }
        return render(request, self.template_name, context)


# store/<int:store_id>/order/<int:order_id>/confirm
class SajjangOrderConfirmView(SajjangRequiredMixin, TemplateView):
    template_name = "/app/sajjang/templates/stores/orders/confirm.html"

    # SajjangOrdersView get 메서드
    def get(self, request, store_id):
        store = Stores.objects.get(id=store_id)
        orders = Order.objects.filter(store_id=store_id)
        context = {"store": store, "orders": orders}
        return render(request, self.template_name, context)


# sajjang/store/<int:store_id>/order/confirm/<int:order_id>
class SajjangOrderConfirmDetailView(SajjangRequiredMixin, TemplateView):
    template_name = "/app/sajjang/templates/stores/orders/confirm_detail.html"

    def get(self, request, store_id, order_id):
        store = Stores.objects.get(id=store_id)
        order = get_object_or_404(Order, id=order_id)
        cart_in_order = Cart.objects.filter(order_id=order_id)
        context = {
            "store": store,
            "order": order,
            "cart_in_order": cart_in_order,
        }
        return render(request, self.template_name, context)


# store/<int:store_id>/order/<int:order_id>/confirm/accept
class SajjangOrderAcceptView(SajjangRequiredMixin, TemplateView):
    def post(self, request, store_id, order_id):
        try:
            order = get_object_or_404(Order, id=order_id)
            order.order_status = "sajjang_accepted"
            order.save()
            return redirect("sajjang:sajjang_store_order", store_id)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


# store/<int:store_id>/order/<int:order_id>/confirm/reject
class SajjangOrderRejectView(SajjangRequiredMixin, TemplateView):
    def post(self, request, store_id, order_id):
        try:
            order = get_object_or_404(Order, id=order_id)
            order.order_status = "sajjang_rejected"
            order.save()
            return redirect("sajjang:sajjang_store_order", store_id)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
