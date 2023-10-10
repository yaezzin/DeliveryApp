from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView
from django.template.loader import render_to_string
from delivery_crew.models import DeliveryHistory


from sajjang.models import Order

# Create your views here.


class DeliveryCrewHomeView(TemplateView):
    template_name = "/app/delivery_crew/templates/home.html"

    def get(self, request):
        orders = Order.objects.filter(is_sajjang_accepted=True)
        context = {"orders": orders}
        return render(request, self.template_name, context)


class DeliveryCrewDeliveryHistory(TemplateView):
    template_name = "/app/delivery_crew/templates/history.html"

    def get(self, request):
        order_history = DeliveryHistory.objects.filter(user_id=request.user.id)
        context = {"orders": order_history}
        return render(request, self.template_name, context)


class DeliveryCrewAcceptView(TemplateView):
    # template_name = "/app/delivery_crew/templates/home.html"

    def post(self, request, order_id):
        delivery = get_object_or_404(Order, pk=order_id)
        new_order_history = DeliveryHistory.objects.create(
            user_id=request.user_id, order_id=delivery.pk
        )
        delivery.delivery_status = True
        delivery.save()
        new_order_history.save()

        return redirect("deliverycrew_home", pk=order_id)


class DeliveryCrewDenyView(TemplateView):
    # template_name = "/app/delivery_crew/templates/home.html"

    def post(self, request, order_id):
        delivery = get_object_or_404(Order, pk=order_id)
        delivery.delivery_status = False
        delivery.save()

        return redirect("deliverycrew_home", pk=order_id)


class DeliveryCrewAlarmView(TemplateView):
    template_name = "/app/delivery_crew/templates/home.html"

    def get(self, request, user_id, **kwargs):
        pending_deliveries = Order.objects.filter(delivery_status=None)
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
