from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from sajjang.models import Category, Stores, Menus
# Create your views here.


class CustomerHomeView(TemplateView):
    def get(self, request):
        category_query = request.GET.get('category', None)
        categories = Category.objects.all()
        if category_query:
            stores = Stores.objects.filter(category_id=category_query)
        else:
            stores = Stores.objects.all()
    
        return render(request, template_name='home.html', context={'categories':categories, 
                                                                    'stores':stores})

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

# /customer/store/
class CustomerStoreView(TemplateView):
    def get(self, request):
        pass

    def post(self, request):
        pass

# /customer/store/<int:store_id>
class CustomerStoreDetailView(TemplateView):
    template_name = 'store/detail.html'

    def get(self, request, store_id):
        store = get_object_or_404(Stores, id=store_id)
        context = {"store": store}
        
        return render(request, self.template_name, context)

# /customer/store/<int:store_id>/menu/
class CustomerStoreMenuView(TemplateView):
    template_name = 'store/menu/list.html'

    def get(self, request, store_id):
        store = get_object_or_404(Stores, id=store_id)
        menus = Menus.objects.filter(store_id=store_id)
        context = {"store": store, "menus": menus}
        return render(request, self.template_name, context)

# /customer/store/<int:stores_id>/menu/{menus_id}
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
