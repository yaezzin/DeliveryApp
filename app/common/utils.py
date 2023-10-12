from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect


class GroupRequiredMixin(UserPassesTestMixin):
    group_name = None

    def test_func(self):
        return self.request.user.groups.filter(name=self.group_name).exists()

    def handle_no_permission(self):
        for group in self.request.user.groups.all():
            if self.request.user.groups.filter(name=group.name).exists():
                return redirect(f"/{group.name}/home")

        return redirect("/")


class CustomerRequiredMixin(GroupRequiredMixin):
    group_name = "customer"


class SajjangRequiredMixin(GroupRequiredMixin):
    group_name = "sajjang"


class DeliveryCrewRequiredMixin(GroupRequiredMixin):
    group_name = "delivery_crew"
