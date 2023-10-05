from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class SajjangHomeView(TemplateView):

    def get(self, request):
        pass


class SajjangStoreView(TemplateView):

    def get(self, request):
        pass


class SajjangStoreAddView(TemplateView):

    def get(self, request):
        pass

    def post(self, request):
        pass


class SajjangStoreDetailView(TemplateView):

    def get(self, request, store_id):
        pass



class SajjangStoreOrderView(TemplateView):

    def get(self, request, store_id):
        pass



class SajjangStoreMenuView(TemplateView):

    def get(self, request, store_id):
        pass



class SajjangStoreMenuItemView(TemplateView):

    def get(self, request, store_id):
        pass
    

class SajjangAddMenuView(TemplateView):

    def get(self, request, store_id):
        pass



class SajjangOrderView(TemplateView):

    def get(self, request):
        pass

