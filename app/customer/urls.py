from django.contrib import admin
from django.urls import path
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from .views import CustomerLoginView, CustomerSignupView, AddressListView

app_name = 'customer'

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', CustomerLoginView.as_view(), name='login')
    # path('logout/', LogoutView.as_view(), name='logout'),
    #path('', login_required(todo.MainView.as_view(), login_url='/login'), name='main'),
]
