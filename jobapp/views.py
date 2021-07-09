from django.shortcuts import render,redirect
from django.views.generic import View,DeleteView,TemplateView,CreateView,ListView,UpdateView,DetailView
from django.urls import reverse_lazy
from .models import UserProfileModel,EmployerProfileModel,MyUserModel,Job,Application
from .forms import AccountCreateForm,EmployerForm,UserProfileForm,SignInForm,JobPostForm
from django.contrib.auth import authenticate,login,logout
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

    # success_url = reverse_lazy("signin")
    # def post(self,request,*args,**kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         role = form.cleaned_data.get("role")
    #         if role=="job seeker":
    #             print("job seekeer")
    #         else:
    #             print("employer")

    success_url = reverse_lazy("signin")


class SigninView(TemplateView):
    model = MyUserModel
    form_class = SignInForm
    template_name = "./jobapp/login.html"
    context={}
    def get(self,request,*args,**kwargs):
        form = self.form_class
        self.context={"form":form}
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request,username=username,password=password)
            if user:
                if user.role == "job seeker":
                    login(request,user)
                    return render(request,"./jobapp/jobseeker.html")
                elif user.role == "Employer":
                    login(request,user)
                    return redirect("employercreate")
            else:
                print(username,password)
                return redirect("signin")
        return redirect("signin")


class SignOutView(View):
    def get(self,request):
        logout(request)
        return redirect("signin")


class UserProfileCreateView(TemplateView):
    model = UserProfileModel
    form_class = UserProfileForm
    template_name = "./jobapp/jobseeker.html"
    context = {}
    def get(self,request,*args,**kwargs):
        form = self.form_class
        self.context["form"]=form
        return render(request,self.template_name,self.context)
# class PostJobView(CreateView):
#     model = Job
#     form_class = JobPostForm

class EmployerProfileCreateView(CreateView):
    model = EmployerProfileModel
    form_class = EmployerForm
    template_name = "./jobapp/Employee.html"
    context = {}


    def get(self,request,*args,**kwargs):
        userhere = MyUserModel.objects.get(user=request.user)
        form = self.form_class(instance=userhere)

        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"./jobapp/viewreg.html")
        return redirect("employercreate")
