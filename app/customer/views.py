from django.shortcuts import render
from .forms import CustomerLoginForm, CustomerSignUpForm, AddressForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, ListView, DetailView, TemplateView
# Create your views here.

class CustomerLoginView(LoginView):
    template_name = 'test_template.html'

class CustomerSignupView(CreateView):
    pass

class AddressListView(ListView):
    pass

    






# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User

# import account.forms as forms

# # Create your views here.

# class MainLoginView(LoginView):
#     form_class = forms.LoginForm
#     template_name = 'login.html'
#     def dispatch(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect('/')
#         return super().dispatch(request, *args, **kwargs)

# class SignupView(CreateView):
#     template_name = 'signup.html'
#     success_url = '/login'
#     form_class = forms.SignUpForm
