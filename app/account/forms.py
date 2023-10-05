from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms


class SigninForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )


class SignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    group_choices = (("customer", "고객"), ("sajjang", "사장"), ("delivery_crew", "배달 크루"))
    group = forms.ChoiceField(label="그룹", choices=group_choices)
