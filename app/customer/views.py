from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class CustomerHomeView(TemplateView):
    def get(self, request):
        pass

    def post(self, request):
        pass

class CustomerSearchCategoryView(TemplateView):
    def get(self, request, category_id):
        pass

    def post(self, request):
        pass

class CustomerAddressView(TemplateView):
    def get(self, request):
        pass

    def post(self, request):
        pass

class CustomerAddressAddView(TemplateView):
    def get(self, request):
        pass

    def post(self, request):
        pass

class CustomerAddressDetailView(TemplateView):
    def get(self, request, address_id):
        pass

class CustomerAddressEditView(TemplateView):
    def get(self, request, address_id):
        pass

    def post(self, request, address_id):
        pass

class CustomerAddressDeleteView(TemplateView):
    def post(self, request, address_id):
        pass    

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

class CustomerCategoryView(TemplateView):
    def get(self, request):
        pass

    def post(self, request):
        pass

class CustomerCategoryDetailView(TemplateView):
    def get(self, request, category_id):
        pass

    def post(self, request, category_id):
        pass


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

