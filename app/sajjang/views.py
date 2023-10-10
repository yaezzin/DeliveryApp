from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.http import JsonResponse
from .models import Stores, Menus, Category, Order
from account.views import SajjangPermissionRequiredMixin


def is_sajjang(user):
    return user.group.filter(name="sajjang").exists()


# /sajjang/home
class SajjangHomeView(TemplateView):
    template_name = "/app/sajjang/templates/home.html"

    def get(self, request):
        stores = Stores.objects.filter(user_id=request.user)
        context = {"stores": stores}
        return render(request, self.template_name, context)


# /sajjang/store/add
class SajjangStoreAddView(TemplateView):
    template_name = "/app/sajjang/template/stores/add.html"

    def get(self, request):
        categories = Category.objects.all()
        context = {"categories": categories}
        return render(request, self.template_name, context)

    def post(self, request):
        try:
            name = request.POST["name"]
            address = request.POST["address"]
            store_pic = request.POST["store_pic"]
            status = request.POST["status"]
            category = Category.objects.get(id=request.POST["category"])
            new_store = Stores(
                user_id=request.user.id,
                name=name,
                address=address,
                store_pic=store_pic,
                status=status,
                category_id=category,
            )
            new_store.save()
            return redirect("sajjang_home")
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


# sajjang/store/<int:store_id>
class SajjangStoreDetailView(TemplateView):
    template_name = "/app/sajjang/templates/stores/store/detail.html"

    def get(self, request, store_id):
        store = get_object_or_404(Stores, id=store_id)
        context = {"store": store}
        return render(request, self.template_name, context)

    def post(self, request, store_id):
        try:
            store = get_object_or_404(Stores, id=store_id)
            store.delete()
            return redirect("sajjang_home")
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


# sajjang/store/<int:store_id>/edit
# sajjang/store/<int:store_id>/delete
class SajjangStoreEditView(TemplateView):
    template_name = "/app/sajjang/templates/stores/store/edit.html"

    def get(self, request, store_id):
        store = get_object_or_404(Stores, id=store_id)
        categories = Category.objects.all()
        context = {"store": store, "categories": categories}
        return render(request, self.template_name, context)

    def post(self, request, store_id):
        try:
            store = get_object_or_404(Stores, id=store_id)
            store.name = request.POST["name"]
            store.address = request.POST["address"]
            store.store_pic = request.POST["store_pic"]
            store.status = request.POST["status"]
            store.category_id = Category.objects.get(id=request.POST["category"])
            store.save()
            return redirect("sajjang_store_detail", store_id=store_id)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


# sajjang/store/<int:store_id>/menu
class SajjangStoreMenuView(TemplateView):
    template_name = "/app/sajjang/templates/stores/store/menu/list.html"

    def get(self, request, store_id):
        menus = Menus.objects.filter(store_id=store_id)
        context = {"menus": menus}
        return render(request, self.template_name, context)


# sajjang/store/<int:store_id>/menu/add
class SajjangAddMenuView(TemplateView):
    template_name = "/app/sajjang/templates/stores/store/menu/add.html"

    def get(self, request, store_id):
        categories = Category.objects.all()
        context = {"categories": categories}
        return render(request, self.template_name, context)

    def post(self, request, store_id):
        try:
            store_id = Stores.objects.get(id=store_id)
            category_id = Category.objects.get(id=request.POST["category"])
            name = request.POST["name"]
            unit_price = request.POST["unit_price"]
            menu_pic = request.POST["menu_pic"]
            is_available = request.POST["is_available"]
            new_menu = Menus(
                store_id=store_id,
                category_id=category_id,
                name=name,
                unit_price=unit_price,
                menu_pic=menu_pic,
                is_available=is_available,
            )
            new_menu.save()
            return redirect("sajjang_store_menu", store_id=store_id)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


# sajjang/store/<int:store_id>/menu/<int:menu_id>
class SajjangStoreMenuDetailView(TemplateView):
    template_name = "/app/sajjang/templates/stores/store/menu/detail.html"

    def get(self, request, store_id, menu_id):
        menu = get_object_or_404(Menus, id=menu_id)
        context = {"menu": menu}
        return render(request, self.template_name, context)

    def post(self, request, store_id, menu_id):
        try:
            menu = get_object_or_404(Menus, id=menu_id)
            menu.delete()
            return redirect("sajjang_store_menu", store_id=store_id)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


# sajjang/store/<int:store_id>/menu/<int:menu_id>/edit
class SajjangEditMenuView(TemplateView):
    template_name = "/app/sajjang/templates/stores/store/menu/edit.html"

    def get(self, request, store_id, menu_id):
        menu = get_object_or_404(Menus, id=menu_id)
        categories = Category.objects.all()
        context = {"menu": menu, "categories": categories}
        return render(request, self.template_name, context)

    def post(self, request, store_id, menu_id):
        try:
            menu = get_object_or_404(Menus, id=menu_id)
            menu.category_id = Category.objects.get(id=request.POST["category"])
            menu.name = request.POST["name"]
            menu.unit_price = request.POST["unit_price"]
            menu.menu_pic = request.POST["menu_pic"]
            menu.is_available = request.POST["is_available"]
            menu.save()
            return redirect(
                "sajjang_store_menu_detail", store_id=store_id, menu_id=menu_id
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


# sajjang/store/<int:store_id>/order
class SajjangOrdersView(TemplateView):
    template_name = "/app/sajjang/templates/stores/orders/list.html"

    def get(self, request, store_id):
        orders = Order.objects.filter(store_id=store_id)
        context = {"orders": orders}
        return render(request, self.template_name, context)


# sajjang/store/<int:store_id>/order/<int:order_id>
class SajjangOrderDetailView(TemplateView):
    template_name = "/app/sajjang/templates/stores/orders/detail.html"

    def get(self, request, store_id, order_id):
        order = get_object_or_404(Order, id=order_id)
        context = {"order": order}
        return render(request, self.template_name, context)


# sajjang/order/<int:order_id>/confirm
class SajjangOrderConfirmView(TemplateView):
    template_name = "/app/sajjang/templates/stores/orders/confirm.html"

    def get(self, request, store_id, order_id):
        order = get_object_or_404(
            Order,
            id=order_id,
            store_id=store_id,
            is_sajjang_accepted=None,
        )
        context = {"order": order}
        return render(request, self.template_name, context)

    def post(self, request, store_id, order_id):
        try:
            order = get_object_or_404(Order, id=order_id)
            order.is_sajjang_accepted = request.POST["is_sajjang_accepted"]
            order.save()
            return redirect("sajjang_store_order")
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


def check_new_order(request):
    store_id = request.data.store_id
    new_orders = Order.objects.filter()
