from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

class CustomerLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), required=True)


class CustomerSignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), required=True)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}), required=True)


class AddressForm(forms.Form):
    addressName = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
    isDefault = forms.CheckboxInput(widget=forms.CheckboxInput(attrs={'class':'form-control'}))