from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class DeliveryCrewHomeView(TemplateView):
    def get(self, request):
        pass


class DeliveryCrewAcceptView(TemplateView):
    def get(self, request, order_id):
        pass


class DeliveryCrewDenyView(TemplateView):
    def get(self, request, order_id):
        pass


class DeliveryCrewAlarmView(TemplateView):
    def get(self, request, user_id):
        pass
