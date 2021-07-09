from .models import Application,Job,MyUserModel,EmployerProfileModel,UserProfileModel
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm


class AccountCreateForm(UserCreationForm):
    class Meta:
        model = MyUserModel
        fields = ["first_name", "last_name","username","password1","password2","phone","gender","role"]


        # car_obj = .objects.create(engine=self.instance)
        # return super(EngineChangeListForm, self).save(*args, **kwargs)

class EmployerForm(ModelForm):
    class Meta:
        model = EmployerProfileModel
        fields = ["company_name","location"]

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfileModel
        fields = ["user","qualification","skills","experience"]

class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class JobPostForm(ModelForm):
    class Meta:
        model = Job
        fields = "__all__"