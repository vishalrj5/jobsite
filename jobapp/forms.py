from .models import MyUserModel,EmployerProfileModel,UserProfileModel
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm


class AccountCreateForm(UserCreationForm):
    class Meta:
        model = MyUserModel
        fields = ["first_name", "last_name","username","password1","password2","phone","gender","role"]

class EmployerForm(ModelForm):
    class Meta:
        model = EmployerProfileModel
        fields = ["company_name","location"]

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfileModel
        fields = ["user","qualification","skills","experience"]
