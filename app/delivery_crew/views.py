from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView
from django.template.loader import render_to_string
from django.db.models import Subquery
from django.contrib.auth.models import Group, User

from sajjang.models import DeliveryHistory, RejectedOrder
from sajjang.models import Order, Stores
from delivery_crew.models import DeliveryLocation
from common.utils import DeliveryCrewRequiredMixin

import requests


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
        crew_active_area = get_object_or_404(
            DeliveryLocation, user_id=request.user.pk
        ).active_area.split(" ")[1]

        orders = (
            Order.objects.filter(order_status="sajjang_accepted")
            .exclude(crew_rejected_order=request.user.id)
            .filter(store_id__address__icontains=crew_active_area)
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


class DeliveryHistoryDetailView(DeliveryCrewRequiredMixin, TemplateView):
    template_name = "/app/delivery_crew/templates/history_detail.html"

    def get(self, request, order_id):
        def get_location_by_address(address):
            url = "https://apis.openapi.sk.com/tmap/pois?version=1&format=json&callback=result"
            params = {
                "appKey": "kyUPwz0Ly2aplTsQ72YKp2EjfDwbI0EJ9KFRwUA4",
                "searchKeyword": address,
                "resCoordType": "WGS84GEO",
                "reqCoordType": "WGS84GEO",
                "count": 1,
            }
            resp = requests.get(url, params=params).json()
            addrInfo = resp["searchPoiInfo"]["pois"]["poi"][0]["newAddressList"][
                "newAddress"
            ][0]
            return (addrInfo["centerLon"], addrInfo["centerLat"])

        order = get_object_or_404(Order, id=order_id)
        context = {"order": order}
        crew_address = get_object_or_404(
            DeliveryLocation, user_id=request.user.pk
        ).address
        cus_address = order.address_id.address

        context["crew_addrLon"], context["crew_addrLat"] = get_location_by_address(
            crew_address
        )
        context["cus_addrLon"], context["cus_addrLat"] = get_location_by_address(
            cus_address
        )

        return render(request, self.template_name, context)

    def post(self, request, order_id):
        pass


class DeliveryCrewDeliveryHistoryPickUp(DeliveryCrewRequiredMixin, TemplateView):
    def post(self, request, order_id):
        def get_location_by_address(address):
            url = "https://apis.openapi.sk.com/tmap/pois?version=1&format=json&callback=result"
            params = {
                "appKey": "kyUPwz0Ly2aplTsQ72YKp2EjfDwbI0EJ9KFRwUA4",
                "searchKeyword": address,
                "resCoordType": "WGS84GEO",
                "reqCoordType": "WGS84GEO",
                "count": 1,
            }
            resp = requests.get(url, params=params).json()
            addrInfo = resp["searchPoiInfo"]["pois"]["poi"][0]["newAddressList"][
                "newAddress"
            ][0]
            return (addrInfo["centerLon"], addrInfo["centerLat"])

        def get_eta(crew_loaction, cus_location):
            url = "https://apis.openapi.sk.com/tmap/routes?version=3&format=json"
            headers = {"appKey": "kyUPwz0Ly2aplTsQ72YKp2EjfDwbI0EJ9KFRwUA4"}
            data = {
                "startX": crew_loaction[0],
                "startY": crew_loaction[1],
                "endX": crew_loaction[0],
                "endY": cus_location[1],
                "reqCoordType": "WGS84GEO",
                "resCoordType": "WGS84GEO",
                "searchOption": "0",
                "trafficInfo": "Y",
                "carType": 7,
                "totalValue": 2,
            }
            resp = requests.post(url, headers=headers, data=data).json()
            eta = resp["features"][0]["properties"]["totalTime"] // 60

            return (10 * (eta // 10)) + 10  # 배달원의 여유시간을 주기 위해 1의 자리 숫자를 없앤 후 10분 추가

        delivery = get_object_or_404(Order, id=order_id)

        crew_address = get_object_or_404(
            DeliveryLocation, user_id=request.user.pk
        ).address
        crew_location = get_location_by_address(crew_address)

        cus_address = delivery.address_id.address
        cus_location = get_location_by_address(cus_address)

        eta = get_eta(crew_location, cus_location)
        delivery.eta = eta
        delivery.order_status = "delivery_in_progress"
        delivery.save()

        return redirect("delivery_crew:delivery_crew_history")


class DeliveryCrewDeliveryHistoryComplete(DeliveryCrewRequiredMixin, TemplateView):
    def post(self, request, order_id):
        delivery = get_object_or_404(Order, id=order_id)
        delivery.order_status = "delivered"
        delivery.save()
        return redirect("delivery_crew:delivery_crew_history")


class DeliveryCrewAcceptView(DeliveryCrewRequiredMixin, TemplateView):
    # template_name = "/app/delivery_crew/templates/home.html"

    def post(self, request, order_id):
        delivery = get_object_or_404(Order, id=order_id)
        delivery_crew = get_object_or_404(User, id=request.user.id)

        new_order_history = DeliveryHistory.objects.create(
            delivery_crew_id=delivery_crew, order_id=delivery
        )
        delivery.order_status = "crew_accepted"
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
