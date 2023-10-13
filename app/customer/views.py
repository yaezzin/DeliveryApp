import stripe, os

from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from customer.models import Cart
from sajjang.models import Category, Stores, Menus, Address, Order
from common.utils import CustomerRequiredMixin

from faker import Faker

fake = Faker("ko_KR")


class CustomerHomeView(CustomerRequiredMixin, TemplateView):
    template_name = "/app/customer/templates/home.html"

    def get(self, request):
        # if request.user.is_authenticated:
        #     users_group = Group.objects.get(user=request.user).name

        #     if users_group == "customer":
        #         category_query = request.GET.get("category", None)
        #         categories = Category.objects.all()

        #         if category_query:
        #             stores = Stores.objects.filter(category_id=category_query)
        #         else:
        #             stores = Stores.objects.all()

        #         search_query = request.GET.get("search", None)
        #         if search_query:
        #             stores = Stores.objects.filter(name__contains=search_query)

        #         return render(
        #             request,
        #             self.template_name,
        #             context={"categories": categories, "stores": stores},
        #         )
        #     else:
        #         return redirect(f"/{users_group}/home")
        # else:
        #     return render(request, self.template_name)

        category_query = request.GET.get("category", None)
        categories = Category.objects.all()
        if category_query:
            stores = Stores.objects.filter(category_id=category_query)
        else:
            stores = Stores.objects.all()

        search_query = request.GET.get("search", None)
        if search_query:
            stores = Stores.objects.filter(name__contains=search_query)

        return render(
            request,
            self.template_name,
            context={"categories": categories, "stores": stores},
        )


# customer/address/
class CustomerAddressView(CustomerRequiredMixin, TemplateView):
    template_name = "/app/customer/templates/address/search.html"

    def get(self, request):
        addresses = Address.objects.filter(customer_id=request.user.pk).order_by(
            "-is_default"
        )
        context = {"addresses": addresses}
        return render(request, self.template_name, context)


# customer/address/add
class CustomerAddressAddView(CustomerRequiredMixin, TemplateView):
    template_name = "/app/customer/templates/address/add.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        try:
            user = User.objects.get(id=request.user.pk)
            address_name = request.POST["address_name"]
            address = request.POST["address"]
            is_default = request.POST.get("is_default", None)

            if is_default:
                is_default = True
            else:
                is_default = False

            new_address = Address(
                customer_id=user,
                address_name=address_name,
                address=address,
                is_default=is_default,
            )
            new_address.save()

            if is_default:
                new_address.set_is_default()

            return redirect("customer:customer_address")
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


# /customer/address/<int:address_id>
class CustomerAddressDetailView(CustomerRequiredMixin, TemplateView):
    template_name = "/app/customer/templates/address/detail.html"

    def get(self, request, address_id):
        address = get_object_or_404(Address, id=address_id)
        context = {"address": address}
        return render(request, self.template_name, context)


# /customer/address/<int:address_id>/edit
class CustomerAddressEditView(CustomerRequiredMixin, TemplateView):
    template_name = "/app/customer/templates/address/edit.html"

    def get(self, request, address_id):
        address = get_object_or_404(Address, id=address_id)
        context = {"address": address}
        return render(request, self.template_name, context)

    def post(self, request, address_id):
        try:
            address = get_object_or_404(Address, id=address_id)
            address.address_name = request.POST["address_name"]
            address.address = request.POST["address"]
            try:
                is_default = request.POST["is_default"]
                if is_default == "on":
                    address.set_is_default()
                else:
                    address.is_default = False
                    address.save()

            except Exception as e:
                address.is_default = False
                address.save()

            return redirect("customer:customer_address_detail", address_id=address_id)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


# /customer/address/<int:address_id>/delete
class CustomerAddressDeleteView(CustomerRequiredMixin, TemplateView):
    template_name = "/app/customer/templates/address/detail.html"

    def post(self, request, address_id):
        delete_address = Address.objects.get(id=address_id)
        delete_address.delete()
        return redirect("customer:customer_address")


# /customer/cart
@method_decorator(csrf_exempt, "dispatch")
class CustomerCartView(CustomerRequiredMixin, TemplateView):
    template_name = "/app/customer/templates/cart/list.html"

    def get(self, request):
        user_carts = Cart.objects.filter(user_id=request.user.pk, order_id=None)
        stores = user_carts.distinct().values_list("store_id")
        context = {"carts": []}
        for store in stores:
            store_name = Stores.objects.filter(id=store[0]).first()
            context["carts"].append(
                {
                    "store_name": store_name,
                    "carts": user_carts.filter(store_id=store[0]).order_by(
                        "-created_at"
                    ),
                }
            )

        return render(request, self.template_name, context)

    def post(self, request):  # javascript 비동기 통신으로만 사용됩니다.
        try:
            cart = get_object_or_404(Cart, id=request.POST["cart_id"])
        except:
            return JsonResponse({"error": "no cart_id"})

        if request.POST["mode"] == "delete":
            cart.delete()
        elif request.POST["mode"] == "quantity_up":
            cart.quantity += 1
            cart.save()
            return JsonResponse(
                {
                    "Success": True,
                    "quantity": cart.quantity,
                    "total_price": cart.get_total_price(),
                }
            )
        elif request.POST["mode"] == "quantity_down":
            cart.quantity -= 1
            if cart.quantity <= 0:
                cart.quantity = 1
            cart.save()
            return JsonResponse(
                {
                    "Success": True,
                    "quantity": cart.quantity,
                    "total_price": cart.get_total_price(),
                }
            )
        elif request.POST["mode"] == "quantity_set":
            pass

        return JsonResponse({"Success": True})


# /customer/orders
class CustomerOrderView(CustomerRequiredMixin, TemplateView):
    template_name = "/app/customer/templates/orders/list.html"

    def get(self, request):
        orders = Order.objects.filter(user_id=request.user.pk)
        context = {"orders": orders}
        return render(request, self.template_name, context)


# /customer/order_create/<int:store_id>
@method_decorator(csrf_exempt, "dispatch")
class CustomerOrderCreateView(CustomerRequiredMixin, TemplateView):
    template_name = "/app/customer/templates/orders/create.html"

    def get(self, request, store_id):
        request.session["store_id"] = store_id

        # 주문 할 메뉴 가져오기
        user_carts = Cart.objects.filter(
            user_id=request.user.pk, order_id=None, store_id=store_id
        ).order_by("-created_at")
        store = user_carts.first().store_id
        context = {"carts": user_carts, "store": store}

        # 주소 목록 가져오기
        addresses = Address.objects.filter(customer_id=request.user.pk).order_by(
            "is_default"
        )
        context["addresses"] = addresses

        # 최종 결제 가격 표시
        pay_price = 0
        for cart in user_carts:
            pay_price += cart.get_total_price()

        context["pay_price"] = pay_price

        return render(request, self.template_name, context)

    def post(self, request, store_id):
        def get_pay_price():
            carts = Cart.objects.filter(
                user_id=request.user.pk, store_id=store_id, order_id=None
            )
            pay_price = 0
            for cart in carts:
                pay_price += cart.get_total_price()
            return pay_price

        try:
            cart = get_object_or_404(Cart, id=request.POST["cart_id"])
        except:
            return JsonResponse({"error": "no cart_id"})

        if request.POST["mode"] == "delete":
            cart.delete()
            return JsonResponse({"Success": True, "pay_price": get_pay_price()})
        elif request.POST["mode"] == "quantity_up":
            cart.quantity += 1
            cart.save()
            return JsonResponse(
                {
                    "Success": True,
                    "quantity": cart.quantity,
                    "total_price": cart.get_total_price(),
                    "pay_price": get_pay_price(),
                }
            )
        elif request.POST["mode"] == "quantity_down":
            cart.quantity -= 1
            if cart.quantity <= 0:
                cart.quantity = 1
            cart.save()
            return JsonResponse(
                {
                    "Success": True,
                    "quantity": cart.quantity,
                    "total_price": cart.get_total_price(),
                    "pay_price": get_pay_price(),
                }
            )
        elif request.POST["mode"] == "quantity_set":
            pass

        return JsonResponse({"Success": True})


# /customer/store/
class CustomerStoreView(CustomerRequiredMixin, TemplateView):
    template_name = "/app/customer/templates/store/search.html"

    def get(self, request):
        stores = Stores.objects.filter(status=True)
        context = {"stores": stores}
        return render(request, self.template_name, context)


# /customer/store/<int:store_id>
class CustomerStoreDetailView(CustomerRequiredMixin, TemplateView):
    template_name = "/app/customer/templates/store/detail.html"

    def get(self, request, store_id):
        store = get_object_or_404(Stores, id=store_id)
        context = {"store": store}
        return render(request, self.template_name, context)


# /customer/store/<int:store_id>/menu/
class CustomerStoreMenuView(CustomerRequiredMixin, TemplateView):
    template_name = "/app/customer/templates/store/menu/list.html"

    def get(self, request, store_id):
        store = get_object_or_404(Stores, id=store_id)
        menus = Menus.objects.filter(store_id=store_id)
        context = {"store": store, "menus": menus}
        return render(request, self.template_name, context)


# /customer/store/<int:stores_id>/menu/{menus_id}
class CustomerMenuDetailView(CustomerRequiredMixin, TemplateView):
    template_name = "/app/customer/templates/store/menu/detail.html"

    def get(self, request, store_id, menu_id):
        menu = get_object_or_404(Menus, id=menu_id)
        context = {"menus": menu}
        return render(request, self.template_name, context)

    def post(self, request, store_id, menu_id):
        try:
            quantity = int(request.POST.get("quantity", 1))

            store = get_object_or_404(Stores, id=store_id)
            menu = get_object_or_404(Menus, id=menu_id)

            cart_item = Cart.objects.filter(
                user_id=request.user, store_id=store, order_id=None, menu_id=menu
            ).last()
            print(cart_item)

            if cart_item:
                cart_item.quantity += quantity
            else:
                cart_item = Cart(
                    user_id=request.user,
                    store_id=store,
                    menu_id=menu,
                    order_id=None,
                    quantity=quantity,
                )
            cart_item.save()
            return redirect("customer:store_menu", store_id=store_id)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


# customer/category/
class CustomerCategoryView(CustomerRequiredMixin, TemplateView):
    template_name = "/app/customer/templates/category/category.html"

    def get(self, request):
        categories = Category.objects.all()
        context = {"categories": categories}
        return render(request, self.template_name, context)


# customer/category/<int:category_id>
class CustomerCategoryDetailView(CustomerRequiredMixin, TemplateView):
    template_name = "/app/customer/templates/category/category.html"

    def get(self, request, category_id):
        category = Category.objects.filter(id=category_id)
        stores = Stores.objects.filter(category_id=category_id)
        context = {"category": category, "stores": stores}
        return render(request, self.template_name, context)


# /customer/order/<int:order_id>
class CustomerOrderDetailView(CustomerRequiredMixin, TemplateView):
    template_name = "/app/customer/templates/orders/detail.html"

    def get(self, request, order_id):
        carts = Cart.objects.filter(order_id=order_id)
        order = get_object_or_404(Order, id=order_id)
        context = {"carts": carts, "order": order}
        return render(request, self.template_name, context)


class CustomerPaymentView(CustomerRequiredMixin, TemplateView):
    # def get(self, request):
    #     template_name = "payment/process.html"
    #     context = {}
    #     context["order"] = Order.objects.filter(id=order_id)
    #     return render(request, template_name=template_name, context=context)

    def post(self, request):
        request.session["address_id"] = int(request.POST["address_id"])

        STRIPE_PUBLISHABLE_KEY = os.getenv("STRIPE_PUBLISHABLE_KEY", "publishable_key")
        STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "secret_key")

        print(STRIPE_SECRET_KEY)
        STRIPE_API_VERSION = os.getenv("STRIPE_API_VERSION", "api_version")

        stripe.api_key = STRIPE_SECRET_KEY
        stripe.api_version = STRIPE_API_VERSION

        success_url = request.build_absolute_uri("/customer/pay_complete")
        cancel_url = request.build_absolute_uri("/customer/pay_cancle")

        session_data = {
            "mode": "payment",
            "client_reference_id": request.user.pk,
            "success_url": success_url,
            "cancel_url": cancel_url,
            "line_items": [],
        }

        orders = Cart.objects.filter(
            user_id=request.user.pk,
            store_id=request.session.get("store_id", None),
            order_id=None,
        )
        for order in orders:
            session_data["line_items"].append(
                {
                    "price_data": {
                        "unit_amount": order.menu_id.unit_price,
                        "currency": "krw",
                        "product_data": {
                            "name": order.menu_id.name,
                        },
                    },
                    "quantity": order.quantity,
                }
            )

        checkout_session = stripe.checkout.Session.create(**session_data)
        return redirect(checkout_session.url, code=303)


class CustomerPayCompletedView(CustomerRequiredMixin, TemplateView):
    template_name = "/app/customer/templates/payment/complete.html"

    def get(self, request):
        store_id_session = request.session.get("store_id", None)
        address_id_session = request.session.get("address_id", None)

        store_id = get_object_or_404(Stores, id=store_id_session)
        address_id = get_object_or_404(Address, id=address_id_session)
        carts = Cart.objects.filter(
            user_id=request.user, store_id=store_id, order_id=None
        )

        total_price = 0
        for cart in carts:
            menu = get_object_or_404(Menus, id=cart.menu_id.pk)
            total_price += menu.unit_price * cart.quantity

        order = Order(
            user_id=request.user,
            store_id=store_id,
            address_id=address_id,
            total_price=total_price,
            order_status="paid",
            receipt=fake.uuid4(),
        )
        order.save()
        carts.update(order_id=order.pk)

        context = {"order_id": order.pk}
        return render(request, self.template_name, context)


class CustomerPayCancledView(CustomerRequiredMixin, TemplateView):
    template_name = "/app/customer/templates/payment/cancle.html"

    def get(self, request):
        store_id_session = request.session.get("store_id", None)
        store_id = get_object_or_404(Stores, id=store_id_session)
        context = {
            "store_id": store_id.pk,
        }
        return render(request, self.template_name, context)
