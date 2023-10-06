from django.contrib.auth.models import User
from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart
from sajjang.models import Category, Stores, Menus, Address
from django.views.generic import TemplateView
from django.http import JsonResponse
# Create your views here.


class CustomerHomeView(TemplateView):
    template_name = "/app/customer/templates/home.html"

    def get(self, request):
        category_query = request.GET.get("category", None)
        categories = Category.objects.all()
        if category_query:
            stores = Stores.objects.filter(category_id=category_query)
        else:
            stores = Stores.objects.all()

        return render(
            request,
            template_name="home.html",
            context={"categories": categories, "stores": stores},
        )


# 미완성
class CustomerSearchCategoryView(TemplateView):
    template_name = "/app/customer/templates/category/category.html"

    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        stores = Stores.objects.get(id=category_id)


class CustomerAddressView(TemplateView):
    template_name = "/app/customer/templates/address/search.html"

    def get(self, request):
        addresses = Address.objects.all()
        context = {"addresses": addresses}
        return render(request, self.template_name, context)


class CustomerAddressAddView(TemplateView):
    template_name = "/app/customer/templates/address/add.html"

    def get(self, request, category_id):
        addresses = Address.objects.all()
        context = {"addresses": addresses}
        return render(request, self.template_name, context)

    def post(self, request):
        try:
            user_id = User.object.get(id=user_id)
            address_name = request.POST["address_name"]
            address = request.POST["address"]
            is_default = request.POST["is_default"]
            new_address = Address(
                address_name=address_name,
                address=address,
                is_default=is_default,
            )
            new_address.save()
            return redirect("customer_address")
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


class CustomerAddressDetailView(TemplateView):
    template_name = "/app/customer/templates/address/detail.html"

    def get(self, request, address_id):
        address = get_object_or_404(Address, id=address_id)
        context = {"address": address}
        return render(request, self.template_name, context)


class CustomerAddressEditView(TemplateView):
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
            address.is_default = request.POST["is_default"]
            address.save()
            return redirect("customer_address_detail", address_id=address_id)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


class CustomerAddressDeleteView(TemplateView):
    def post(self, request, address_id):
        delete_address = Address.objects.get(id=address_id)
        delete_address.delete()

        return redirect("customer_address")


class CustomerCartView(TemplateView):
    def get(self, request):
        pass

    def post(self, request):
        pass


class CustomerOrderView(TemplateView):
    def get(self, request):
        pass

    def post(self, request):
        pass


class CustomerOrderCreateView(TemplateView):
    def post(self, request, id):
        pass

# /customer/store/
class CustomerStoreView(TemplateView):
    template_name = '/app/customer/templates/store/search.html'

    def get(self, request):
        stores = Stores.objects.filter(status=True)
        context = {"stores" : stores}
        return render(request, self.template_name, context)

# /customer/store/<int:store_id>
class CustomerStoreDetailView(TemplateView):
    template_name = '/app/customer/templates/store/detail.html'

    def get(self, request, store_id):
        store = get_object_or_404(Stores, id=store_id)
        context = {"store": store}      
        return render(request, self.template_name, context)

# /customer/store/<int:store_id>/menu/
class CustomerStoreMenuView(TemplateView):
    template_name = '/app/customer/templates/store/menu/list.html'

    def get(self, request, store_id):
        store = get_object_or_404(Stores, id=store_id)
        menus = Menus.objects.filter(store_id=store_id)
        context = {"store": store, "menus": menus}
        return render(request, self.template_name, context)

# /customer/store/<int:stores_id>/menu/{menus_id}
class CustomerMenuDetailView(TemplateView):
    template_name = '/app/customer/templates/store/menu/detail.html'

    def get(self, request, store_id, menu_id):
        menu = get_object_or_404(Menus, id=menu_id)
        context = {"menu": menu}
        return render(request, self.template_name, context)

    def post(self, request, store_id, menu_id):
        try:
            quantity = request.POST.get('quantity')
            unit_price = request.POST.get('unit_price')
            
            store = get_object_or_404(Stores, id=store_id)
            menu = get_object_or_404(Menus, id=menu_id)

            cart_item = Cart(
                user_id=request.user.pk,
                stores_id=store,
                menus_id=menu,
                order_id=None,
                quantity=quantity,
                unit_price=unit_price
            )
            cart_item.save()
            return redirect("store_menu", store_id=store_id)
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

# customer/category/
class CustomerCategoryView(TemplateView):
    template_name = "/app/customer/templates/category/category.html"
    
    def get(self, request):
        categories = Category.objects.all()
        context = {"categories": categories}
        return render(request, self.template_name, context)

# customer/category/<int:category_id>
class CustomerCategoryDetailView(TemplateView):
    template_name = "/app/customer/templates/category/category.html"
    
    def get(self, request, category_id):
        category = Category.objects.filter(id=category_id)
        stores = Stores.objects.filter(category_id=category_id)
        context = {"category": category, "stores": stores}
        return render(request, self.template_name, context)


class CustomerOrderDetailView(TemplateView):
    def get(self, request, order_id):
        pass


class CustomerPaymentView(TemplateView):
    def get(self, request):
        pass

    def post(self, request):
        pass


class CustomerPayCompletedView(TemplateView):
    def get(self, request):
        pass

    def post(self, request):
        pass
