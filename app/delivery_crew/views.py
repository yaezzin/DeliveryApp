from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView
from django.template.loader import render_to_string
from django.db.models import Subquery
from django.contrib.auth.models import Group, User

from sajjang.models import DeliveryHistory, RejectedOrder
from sajjang.models import Order, Stores
from common.utils import DeliveryCrewRequiredMixin


class DeliveryCrewHomeView(DeliveryCrewRequiredMixin, TemplateView):
    template_name = "/app/delivery_crew/templates/home.html"

    def get(self, request):
        # if request.user.is_authenticated:
        #     users_group = Group.objects.get(user=request.user).name

        #     if users_group == "delivery_crew":
        #         orders = Order.objects.filter(
        #             order_status="sajjang_accepted").exclude(crew_rejected_order=request.user.id)
        #         stores = Stores.objects.filter(
        #             id__in=Subquery(orders.values("store_id"))
        #         )
        #         context = {"orders": orders, "stores": stores}
        #         return render(request, self.template_name, context)
        #     else:
        #         return redirect(f"/{users_group}/home")
        # else:
        #     return render(request, self.template_name)

        orders = Order.objects.filter(order_status="sajjang_accepted").exclude(
            crew_rejected_order=request.user.id
        )
        stores = Stores.objects.filter(id__in=Subquery(orders.values("store_id")))
        context = {"orders": orders, "stores": stores}
        return render(request, self.template_name, context)


class DeliveryCrewDeliveryHistory(DeliveryCrewRequiredMixin, TemplateView):
    template_name = "/app/delivery_crew/templates/history.html"

    def get(self, request):
        order_history = DeliveryHistory.objects.filter(delivery_crew_id=request.user.id)
        print(order_history)
        context = {"order_histories": order_history}
        return render(request, self.template_name, context)


class DeliveryCrewAcceptView(DeliveryCrewRequiredMixin, TemplateView):
    # template_name = "/app/delivery_crew/templates/home.html"

    def post(self, request, order_id):
        delivery = get_object_or_404(Order, id=order_id)
        delivery_crew = get_object_or_404(User, id=request.user.id)

        new_order_history = DeliveryHistory.objects.create(
            delivery_crew_id=delivery_crew, order_id=delivery
        )
        delivery.order_status = "delivery_accepted"
        delivery.save()
        new_order_history.save()

        return redirect("delivery_crew:delivery_crew_home")


class DeliveryCrewDenyView(DeliveryCrewRequiredMixin, TemplateView):
    # template_name = "/app/delivery_crew/templates/home.html"

    def post(self, request, order_id):
        delivery_order = get_object_or_404(Order, id=order_id)
        delivery_crew = get_object_or_404(User, id=request.user.id)

        reject = RejectedOrder.objects.create(
            delivery_crew_id=delivery_crew, order_id=delivery_order
        )

        reject.save()

        return redirect("delivery_crew:delivery_crew_home")


class DeliveryCrewAlarmView(DeliveryCrewRequiredMixin, TemplateView):
    # template_name = "/app/delivery_crew/templates/home.html"

    def get(self, request, user_id, **kwargs):
        pending_deliveries = Order.objects.filter(order_status="sajjang_accepted")
        context = super().get_context_data(**kwargs)
        context["pending_deliveries"] = pending_deliveries
        return context

    def render_to_response(self, context, **response_kwargs):
        # AJAX 요청의 응답으로 JSON 데이터 반환
        pending_deliveries = context["pending_deliveries"]
        alerts_html = render_to_string(
            "delivery_crew/alert_list.html", {"pending_deliveries": pending_deliveries}
        )
        return JsonResponse({"html": alerts_html})
