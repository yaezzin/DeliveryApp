from django.shortcuts import render, redirect, get_object_or_404
from multiprocessing import context
from django.views.generic import TemplateView
from sajjang.models import Category, Stores, Address, User
from django.http import JsonResponse

# Create your views here.


class CustomerHomeView(TemplateView):
    template_name = "home.html"

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
    template_name = "category/category.html"

    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        stores = Stores.objects.get(id=category_id)


class CustomerAddressView(TemplateView):
    template_name = "address/search.html"

    def get(self, request):
        addresses = Address.objects.all()
        context = {"addresses": addresses}
        return render(request, self.template_name, context)


class CustomerAddressAddView(TemplateView):
    template_name = "address/add.html"

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
    template_name = "address/detail.html"

    def get(self, request, address_id):
        address = get_object_or_404(Address, id=address_id)
        context = {"address": address}
        return render(request, self.template_name, context)


class CustomerAddressEditView(TemplateView):
    template_name = "address/edit.html"

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


class CustomerStoreView(TemplateView):
    def get(self, request):
        pass

    def post(self, request):
        pass


class CustomerStoreDetailView(TemplateView):
    def get(self, request, stores_id):
        pass


class CustomerStoreMenuView(TemplateView):
    def get(self, request, stores_id):
        pass


class CustomerMenuDetailView(TemplateView):
    def get(self, request, stores_id, menus_id):
        pass

    def post(self, request, stores_id, menus_id):
        pass

# customer/category/
class CustomerCategoryView(TemplateView):
    template_name = "category/category.html"
    
    def get(self, request):
        categories = Category.objects.all()
        context = {"categories": categories}
        return render(request, self.template_name, context)

# customer/category/<int:category_id>
class CustomerCategoryDetailView(TemplateView):
    template_name = "category/category.html"
    
    def get(self, request, category_id):
        category = Category.objects.filter(id=category_id)
        context = {"category": category}
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
