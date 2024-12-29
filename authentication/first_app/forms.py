from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class SignupForm(UserCreationForm):
    first_name = forms.CharField(required=True,widget=forms.TextInput())
    last_name = forms.CharField(required=True,widget=forms.TextInput())
    email = forms.CharField(required=True,widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ChangeUserdata(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']