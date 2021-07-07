from django.shortcuts import render
from django.views.generic import DeleteView,TemplateView,CreateView,ListView,UpdateView,DetailView
from django.urls import reverse_lazy
from .models import UserProfileModel,EmployerProfileModel,MyUserModel
from .forms import AccountCreateForm,EmployerForm,UserProfileForm
from django.forms import forms
# Create your views here.
# class Employee(CreateView):
#     model = UserProfileModel
#     form_class = UserProfileForm
#     template_name = "./jobapp/Employee.html"
#     success_url = reverse_lazy("signin")
#     # context = {}
#     # def get(self, request, *args, **kwargs):
#     #     form = self.form_class()
#     #     self.context["form"] = form
#     #     print("okay")
#     #     return render(request, self.template_name, self.context)


class UserRegView(CreateView):
    model = MyUserModel
    form_class = AccountCreateForm
    template_name = "./jobapp/register.html"
    success_url = reverse_lazy("signin")



