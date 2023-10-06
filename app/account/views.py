from typing import Any
from django import http
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView
import account.forms as forms


# Create your views here.


class SigninView(TemplateView):
    def get(self, request):
        form = forms.SigninForm()

        return render(request, template_name="signin.html", context={"form": form})

    def post(self, request):
        form = forms.SigninForm(request.POST)
        # print(form.cleaned_data['username'])

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                users_group = Group.objects.get(user=user).name
                print(users_group)

                return redirect(f'/{users_group}/home')

        return redirect("/")


class SignupView(TemplateView):
    def get(self, request):
        form = forms.SignUpForm()

        return render(request, template_name="signup.html", context={"form": form})

    def post(self, request):
        form = forms.SignUpForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]

            if password1 == password2:
                user = User.objects.create_user(username=username, password=password2)
                group = Group.objects.get(name=form.cleaned_data["group"])
                user.groups.add(group)

                return redirect("/")


class GroupPermissionRequiredBaseMixin:
    def has_group_permission(self, user, group_name, permission_codename):
        # try:
        #     users_group = Group.objects.get(user=user)
        #     print(users_group)

        #     return users_group

        # except Group.DoesNotExist:
        #     return False  # 그룹이 존재하지 않으면 False 반환

        # if user in group.user_set.all() and user.has_perm(permission_codename):
        #     return True  # 사용자가 그룹에 속하고 퍼미션을 가지고 있으면 True 반환

        # return False  # 그룹 퍼미션을 만족하지 못하면 False 반환

        try:
            users_group = Group.objects.get(user=user)
            print(users_group)
            print("======       ", str(users_group) == str(group_name))
            print(str(users_group))
            print(str(group_name))
            print("=========")

            if str(users_group) == str(group_name):
                return True

        except Group.DoesNotExist:
            return False  # 그룹이 존재하지 않으면 False 반환

    def dispatch(self, request, *args, **kwargs):
        if not self.has_group_permission(
            request.user, "customer", "myapp.can_access_group"
        ):
            raise PermissionDenied  # 그룹 퍼미션을 확인하고 접근을 거부할 경우 예외 발생
        return super().dispatch(request, *args, **kwargs)


class CustomerPermissionRequiredMixin:
    def has_group_permission(self, user, group_name, permission_codename):
        try:
            users_group = Group.objects.get(user=user)
            print(users_group)
            print("======       ", str(users_group) == str(group_name))
            print(str(users_group))
            print(str(group_name))
            print("=========")

            if str(users_group) == str(group_name):
                return True

        except Group.DoesNotExist:
            return False  # 그룹이 존재하지 않으면 False 반환

    def dispatch(self, request, *args, **kwargs):
        if not self.has_group_permission(
            request.user, "customer", "access_customer_page"
        ):
            raise PermissionDenied  # 그룹 퍼미션을 확인하고 접근을 거부할 경우 예외 발생
        return super().dispatch(request, *args, **kwargs)


class SajjangPermissionRequiredMixin:
    def has_group_permission(self, user, group_name, permission_codename):
        try:
            users_group = Group.objects.get(user=user)
            print(users_group)
            print("======       ", str(users_group) == str(group_name))
            print(str(users_group))
            print(str(group_name))
            print("=========")

            if str(users_group) == str(group_name):
                return True

        except Group.DoesNotExist:
            return False  # 그룹이 존재하지 않으면 False 반환

    def dispatch(self, request, *args, **kwargs):
        if not self.has_group_permission(
            request.user, "sajjang", "access_sajjang_page"
        ):
            raise PermissionDenied  # 그룹 퍼미션을 확인하고 접근을 거부할 경우 예외 발생
        return super().dispatch(request, *args, **kwargs)


class DeliveryCrewPermissionRequiredMixin:
    def has_group_permission(self, user, group_name, permission_codename):
        try:
            users_group = Group.objects.get(user=user)
            print(users_group)
            print("======       ", str(users_group) == str(group_name))
            print(str(users_group))
            print(str(group_name))
            print("=========")

            if str(users_group) == str(group_name):
                return True

        except Group.DoesNotExist:
            return False  # 그룹이 존재하지 않으면 False 반환

    def dispatch(self, request, *args, **kwargs):
        if not self.has_group_permission(
            request.user, "delivery_crew", "access_delivery_crew_page"
        ):
            raise PermissionDenied  # 그룹 퍼미션을 확인하고 접근을 거부할 경우 예외 발생
        return super().dispatch(request, *args, **kwargs)


class CustomerView(LoginRequiredMixin, CustomerPermissionRequiredMixin, TemplateView):
    template_name = "customer/main.html"
    login_url = "/"


class SajjangView(LoginRequiredMixin, SajjangPermissionRequiredMixin, TemplateView):
    template_name = "sajjang/main.html"
    login_url = "/"


class DeliveryCrewView(
    LoginRequiredMixin, DeliveryCrewPermissionRequiredMixin, TemplateView
):
    template_name = "delivery/crew_main.html"
    login_url = "/"
